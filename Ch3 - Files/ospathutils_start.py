#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path  # pathlib.path is now preferred for accessing path functionality
import datetime
from datetime import date, time, timedelta
import time


def main():
    # Print the name of the OS
    # print(os.name)

    # # Check for item existence and type
    # print("This file exists: ", str(path.exists(".\myFile.txt")))
    # print("This is a file: ", str(path.isfile(".\myFile.txt")))
    # print("This is a directory: ", str(path.isdir(".\myFile.txt")))

    # # Work with file paths
    # print("File path is: ", str(path.realpath(".\myFile.txt")))
    # print("This file's path and file name are: ", str(
    #     path.split(path.realpath(".\myFile.txt"))))
    
    # Get the modification time
    t = time.ctime(path.getmtime("myFile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("myFile.txt")))
    
    # Calculate how long ago the item was modified
    dm = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("myFile.txt"))
    print("File last modified: ", dm)
    print("Rephrased, it has been ", dm.total_seconds(),
          " since it was last modified.")
  
if __name__ == "__main__":
    main()
