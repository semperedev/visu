#!/usr/bin/env python3

"""
Description: Check if all the images are present.
Author: P. Sempere (sempere.dev)
"""

from glob import glob
from json import load
from os.path import exists


errors = 0

filenames = set()

with open('data.json') as fp:
    for obj in load(fp):
        filename = 'media/' + obj['image']

        filenames.add(filename)

        if not exists(filename):
            print(f'Image not found: {obj["image"]} [{obj["name"]} - {obj["family"]} - {obj["discoverer"]}]')
            errors += 1

for image in glob('media/**', recursive=True):
    if '.' in image and image not in filenames:
        print(f'Image {image} is not used')
        errors += 1

if errors:
    print(f'Finished with {errors} errors!')
    exit(1)
else:
    print('All images checked successfuly!')
