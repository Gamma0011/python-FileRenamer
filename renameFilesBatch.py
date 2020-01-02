#! /usr/bin/python
# SH - 12/20/2019

import os
import re


def changeFileNames(workingFolder):
    os.chdir(workingFolder)
    i = 1
    for file in os.listdir():
        src = file.lower()
        # ignore all chracters other than those included in the regex
        dst = re.sub('[^A-Za-z0-9.]+', "", src)
        os.rename(src, dst)
        i = i + 1


# user input of directory with pre-renamed files
workingFolder = input("\nWhich directory has the files you want to rename?\n")

changeFileNames(workingFolder)

print("File names changed.")
