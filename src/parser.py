import re

# JS/TS Search Patterns
# Finds hex integers, ignoring quoted strings
JS_HEX_PATTERN = r'(?<!["\'])\b0x[0-9a-fA-F]+\b(?!["\'])'
# Finds decimal integers, ignoring quoted strings
JS_DEC_PATTERN = r'(?<!["\'])\b\d+\b(?!["\'])'


def js_ts_converter(path: str, reverse=False, backup=False, test=False):

    def dec_to_hex(match):
        dec = int(match.group(0))
        hexstr = hex(dec)
        return hexstr

    def hex_to_dec(match):
        hex = match.group(0)
        dec = int(hex, 16)
        return str(dec)

    # Original Contents
    content = ""

    # Processed String
    result = ""

    # Open the contents of the file
    with open(path, "r", encoding="utf8") as file:

        # Parse the file contents
        content = file.read()

        if reverse:
            # Convert all hex values to decimal
            result = re.sub(JS_DEC_PATTERN, dec_to_hex, content)
        else:
            # Convert all hex values to decimal
            result = re.sub(JS_HEX_PATTERN, hex_to_dec, content)

    # Content has changed
    if content != result:
        # Test switch
        if test:
            print(f"MODIFY: {path}")
        else:

            if backup:
                # Backup old file
                newpath = f"{path}.bak"
                with open(newpath, "w", encoding="utf8") as newfile:
                    newfile.write(content)

            # Overwrite the original file
            with open(path, "w", encoding="utf8") as file:
                file.write(result)


SUBPROCESSES = {
    "js": js_ts_converter,
    "ts": js_ts_converter,
}

SUPPORTED_FILE_TYPES = list(SUBPROCESSES.keys())
