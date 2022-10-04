#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#


from tkinter import W


def main():
    # # Open a file for writing (w) and create it if it doesn't exist (+). Subsequent runs will overwrite the existing file, if present.
    # #myFile = open("myFile.txt", "w+")

    # # Open the file for appending text to the end;
    # myFile = open("myFile.txt", "a+")

    # # write some lines of data to the file
    # myFile.write("This is new text I have added through code with Append.\n")

    # # close the file when done; must be paired with any file open() call.  Can be skipped using the with() accessor instead of open()
    # myFile.close()

    # Open the file back up and read the contents; do not need to use file.close() when reading a file.
    # .read() gives the contents of the file as they are; .readlines() returns an object containing each line as an element
    myFile = open("myFile.txt", "r")
    if myFile.mode == 'r':
        myText = myFile.read()
        print(myText)


if __name__ == "__main__":
    main()
