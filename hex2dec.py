import argparse

# Import Hex to Dec Converter
from src.common import filter_files, get_files, get_suffixes
from src.parser import SUBPROCESSES, SUPPORTED_FILE_TYPES

# Create the parser
parser = argparse.ArgumentParser(
    description="Recursive Hexidecimal to Decimal Converter"
)
parser.add_argument("path", nargs="*", type=str, help="Paths to process", default=["."])
parser.add_argument("--exclude", "-x", type=str, help="Strings to exclude", default="")
parser.add_argument("--include", "-i", type=str, help="Strings to include", default="")
parser.add_argument(
    "--reverse", "-r", action="store_true", help="Convert integers from decimal to hex"
)
parser.add_argument(
    "--test", "-t", action="store_true", help="Test, does not convert anything"
)
parser.add_argument(
    "--backup", "-b", action="store_true", help="Back-up any modified files"
)


def main(args):

    # Process inclusions/exclusions
    include = args.include.split(",")
    exclude = args.exclude.split(",")

    # Loop over each path
    for path in args.path:

        print(f"Processing path '{path}' ...")

        # Get all subfiles
        all_files = get_files(path)

        # Filter out excluded files
        files = filter_files(all_files, include, exclude)

        # Loop over each file
        for file in files:
            ext = get_suffixes(file)

            # If the extension is supported
            if ext in SUPPORTED_FILE_TYPES:
                SUBPROCESSES[ext](file, args.reverse, args.backup, args.test)


if __name__ == "__main__":

    # Parse the arguments
    args = parser.parse_args()

    main(args)
