#
# Example file for working with filesystem shell methods
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    # make a duplicate of an existing file
    if path.exists("myfile.txt.bak"):
        # get the path to the file in the current directory
        fp = path.realpath("./myFile.txt")
        
    # let's make a backup copy by appending "bak" to the name
        dest = fp + ".bak"
        #shutil.copy(fp, dest)
    # rename the original file
        #os.rename("./myFile.txt", "./newFile.txt")
        # now put things into a ZIP archive
        # root_dir, file = path.split(fp)
        # make_archive("myZipFile", "zip", root_dir)
    # more fine-grained control over ZIP files
        with ZipFile("testzip.7z", "w") as newzip:
            newzip.write("./newFile.txt")
            newzip.write("./myFile.txt.bak")
      
if __name__ == "__main__":
    main()
