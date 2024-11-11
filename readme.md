# Recursive Hexadecimal to Decimal Converter
### Created By Damon Murdoch ([@SirScrubbington](https://github.com/SirScrubbington))

## Description

This is a command-line tool that recursively searches files in specified directories, converting hexadecimal values to decimal (or vice versa if `--reverse` is specified). It currently supports JavaScript and TypeScript files, with additional language support planned in the future. The script also provides options to test without making changes, backup modified files, and filter files based on inclusion and exclusion criteria.

## Table of Contents

- [Usage](#usage)
- [Future Changes](#future-changes)
- [Problems / Improvements](#problems--improvements)
- [Changelog](#changelog)
- [Sponsor this Project](#sponsor-this-project)
- [License](#license)

## Usage

The script provides several arguments to customize the behavior:

```bash
python convert.py [path(s)] [options]
```

### Arguments

- `path(s)`: One or more directories to recursively process. Defaults to the current directory (`.`) if none are provided.

### Options

- `--exclude`, `-x`: Comma-separated list of strings. Files containing any of these strings in their path will be excluded.
- `--include`, `-i`: Comma-separated list of strings. Only files containing any of these strings in their path will be included.
- `--reverse`, `-r`: Converts integers from decimal to hexadecimal.
- `--test`, `-t`: Runs in test mode, where no files are modified.
- `--backup`, `-b`: Creates a backup for each modified file.

### Example Commands

To convert hexadecimal values to decimal in the current directory and create backups of modified files:

```bash
python convert.py -b
```

To convert decimal values to hexadecimal, excluding files with specific strings in their path:

```bash
python convert.py ./src ./docs -r -x exclude_this,ignore_that
```

To run in test mode, only including files with certain strings in their path:

```bash
python convert.py -t -i "include_this,another_include"
```

## Future Changes

Planned updates for the tool include:

### Change Table

| Change Description                       | Priority |
| ---------------------------------------- | -------- |
| Support additional file types (e.g., .py, .json) | High     |
| Improve logging and error handling       | Medium   |
| Add verbose mode for detailed output     | Low      |

## Problems / Improvements

For any suggestions, issues, or improvements, please feel free to open an issue [here](../../issues) or message me on Twitter with the details of the issue and reproduction steps.

## Changelog

### Ver. 0.0.1

- Initial release with support for JavaScript and TypeScript.
- Features include path processing, inclusion/exclusion filters, reverse conversion, backup, and test mode.

## Sponsor this Project

If you'd like to support this project and future updates, feel free to use the PayPal donation link below:
[https://www.paypal.com/paypalme/sirsc](https://www.paypal.com/paypalme/sirsc)

## License

Distributed under the MIT License. See `LICENSE` for more information.
