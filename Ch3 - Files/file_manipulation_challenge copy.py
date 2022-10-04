'''In this challenge, the following will occur:
Create a new directory
Create a new file, within the new directory
Write a list of all files inside of the base directory into the new file; including the total byte count of all files in the directory

personal challenge: Do it with pathlib, not path

'''
import os
import pathlib
from pathlib import Path, PurePath, PureWindowsPath, WindowsPath
from posixpath import split

'''Define the new directory, within the current working directory'''
resultsPath = Path.cwd() / "results"

'''Create new directory; create any non-existent parent directories and suppress duplicate file error if dir exists'''
resultsPath.mkdir(parents=True, exist_ok=True)

'''Create file in new directory and write contents of parent directory to the file'''
resultsFile = Path(resultsPath, "results.txt")
resultsFile.touch(exist_ok=True)

'''Get list of all files in cwd; check for file names already in results.txt, and write file names to results.txt if they are not already present'''
eLines = resultsFile.open().read().split('\n')
pathList = resultsPath.parent.iterdir()
# print(dir(fl))
totalSize = 0

# for f in pathList:
#     totalSize = int(totalSize + f.stat().st_size)
#     # print(f"Total file size: {totalSize} bytes")

# for f in pathList:
#     totalSize = int(totalSize + f.stat().st_size)
#     if f.is_file():
#         with resultsFile.open(mode="a") as rf:
#             if f.name in eLines:
#                 continue
#             else:
#                 rf.write(f.name+"\n")


# with resultsFile.open(mode="a") as rf:
#     rf.write(
#         f"_______________________________________\n Total Byte size is: {totalSize}kB")
resultsFile.unlink()
for f in pathList:
    totalSize = int(totalSize + f.stat().st_size)
    if f.is_file():
        with resultsFile.open(mode="a") as rf:
            rf.write(f.name+"\n")


with resultsFile.open(mode="a") as rf:
    rf.write(
        f"_______________________________________\n Total Byte size is: {totalSize}kB")
