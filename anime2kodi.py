# Script to rename a directory of video and subtitle files for use
# with Kodi Media Center.

import os
import glob
import re


def main():
    path = input("Enter path to files: ")
    type = ('*.mp4', '*.mkv', '*.ass')
    file_list = []

    os.chdir(path)
    # print(os.getcwd())

    for file in type:
        file_list.extend(glob.glob(file))
        # first = file_list[1]

    msgexp = """
    MetaCharacters; escape using \\
    . ^ $ * + ? {} [] \ | ()

    .	- Any character except new line
    \d	- Digit (0-9); not \D
    \w	- Word character (a-z, A-Z, 0-9, _); not \W
    \s	- Whitespace (space, tab, newline); not \S
    \\b	- Word boundary; not \B
    ^	- Begginning of string (line)
    $	- End of string
    []	- Matches character in brackets; not [^ ]
    |	- Either or
    ()	- Group
    *	- 0 or more
    +	- 1 or more
    ?	- 0 or one
    {3}	- Exact number
    {3,4} - Range of number (min, max)

    Enter for default: (.*)( Episode )(\d+)(.*)(\.mp4|\.mkv|\.ass)
    """

    print(msgexp)
    expression = input("Enter a regular expression: ") or \
        "(.*)( Episode )(\d+)(.*)(\.mp4|\.mkv|\.ass)"

    msggrp = """
    Enter the value or group (\\\\#) for each
    or enter for default:
        Series = \\\\1
        Season = 1
        Episode = \\\\3
        File extension = \\\\5
    """

    print(msggrp)
    series_grp = input("Series group: ") or "\\1"
    season = input("Season value: ") or "1"
    episode_grp = input("Episode group: ") or "\\3"
    extension_grp = input("Extension group: ") or "\\5"

    for old in file_list:
        series = re.sub(expression, series_grp, old)
        episode = re.sub(expression, episode_grp, old)
        extension = re.sub(expression, extension_grp, old)
        new = series + ".s" + season.zfill(2) + "e" + episode.zfill(2) \
            + extension
        os.rename(old, new)

    for new_list in os.listdir('.'):
        print(new_list)


main()
