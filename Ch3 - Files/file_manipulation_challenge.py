'''In this challenge, the following will occur:
Create a new directory
Create a new file, within the new directory
Write a list of all files inside of the base directory into the new file; including the total byte count of all files in the directory

personal challenge: Do it with pathlib, not path

'''
from genericpath import isfile
import os
import pathlib
from pathlib import Path, PurePath, PureWindowsPath, WindowsPath
from posixpath import split

'''Create the new directory within the current working directory'''
myPath = Path.cwd() / "results"

'''Create new directory; create any non-existent parent directories and suppress duplicate file error if dir exists'''
myPath.mkdir(parents=True, exist_ok=True)

'''Create file in new directory and write contents of parent directory to the file'''
resFile = Path(myPath, "results.txt")
resFile.touch(exist_ok=True)

'''Get list of all files in cwd; check for file names already in results.txt, and write file names to results.txt if they are not already present'''
eLines = resFile.open().read().split('\n')
fl = myPath.parent.iterdir()
# print(list(fl))

for f in fl:
    with resFile.open(mode="a") as rf:
        if f.name in eLines:
            # print(f'{f.name} is in eLines')
            continue
        else:
            # print(f'{f.name} is NOT in eLines')
            rf.write(f.name+"\n")
