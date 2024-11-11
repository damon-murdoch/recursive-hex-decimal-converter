from pathlib import Path
from typing import List


def get_files(path: str):
    return [str(file) for file in Path(path).rglob("*") if file.is_file()]


def get_suffixes(path: str):
    return ".".join(Path(path).suffixes)[1:]


def filter_files(files: List[str], include: List[str], exclude: List[str]):
    filtered_lists = []

    for file in files:
        included = True

        # Check for inclusions
        for inclusion in include:
            if inclusion not in file:
                included = False
                break

        # Still included
        if included:
            # Check for exclusions
            for exclusion in exclude:
                if exclusion in file:
                    included = False
                    break

        # Add to list
        if included:
            filtered_lists.append(file)

    return filtered_lists
