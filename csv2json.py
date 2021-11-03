#!/usr/bin/env python3

"""
Description: Converts CSV entries to JSON objects.
Author: P. Sempere (sempere.dev)
"""

import sys
from json import dump

OUTPUT_FILE = 'data.json'
HEADERS = ('name', 'family', 'discoverer', 'image')

data = []
files_count = 0
read_count = 0

for file in sys.argv[1:]:
    try:
        with open(file, 'r') as fp:
            fp.readline() # To remove the headers

            for line in fp.readlines():
                obj = {}

                for index, value in enumerate(line.strip('\r\n').split(',')):
                    obj[HEADERS[index]] = value

                data.append(obj)

                read_count += 1

            files_count += 1
    except IOError:
        print(f'Error! Could not read file {file}')

print(f'Read {read_count} lines from {files_count} files!')

try:
    with open('data.json', 'w') as fp:
        dump(data, fp)

    print(f'All objects written successfully to {OUTPUT_FILE}')
except IOError:
    print(f'Error! Could not write to {OUTPUT_FILE}')
