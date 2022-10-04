#
# Example file for working with loops
# LinkedIn Learning Python course by Joe Marini
#


def main():
    # x = 0

    # # TODO: define a while loop
    # while x < 5:
    #     print(x)
    #     x += 1


    # TODO: define a for loop
    # for x in range(5, 10):
    #     print(x)

    # TODO: use a for loop over a collection
    # days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    # print(f"days is {len(days)} items long")
    # print("days is {} items long.".format(len(days)))
    # for day in days:
    #     print(day)

    # TODO: use the break and continue statements


    # TODO: using the enumerate() function to get index 
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i, d in enumerate(days):
        print(i, d)

    for i, d in enumerate(days):
        if i % 2 == 0:
            print(i)
        else:
            print(f"Nope, it's {d}")

if __name__ == "__main__":
    main()
