'''
Create a function that asks for user input, checks whether the input is a palindrome and reports the result.
It should, also, check for the word 'exit' and terminate the program when it is entered.
'''


def palCheck():

    while True:
        palInput = input(
            "Enter a potential plaindrome to check, or type 'exit' to quit: ")
        if palInput == 'exit':
            break
        else:
            # compString = ""
            # for i in palInput.lower():
            #     if i.isalnum():
            #         compString = compString + i

            #Take the input string (palInput), check each element to make sure it is alphanumeric,
            # #convert to lower case and add to a new string (compString).  Removes spaces and punctuation
            compString = ''.join(filter(str.isalnum, palInput)).lower()

            # if compString == compString[::-1] and len(compString) != 0:
            #     print(f"Yes! {palInput} is a palindrome; congratulations!")
            # elif compString != compString[::-1] and len(compString) != 0:
            #     print(
            #         f"I'm sorry; {palInput} is not a palindrome. Please try again.")
            # else:
            #     print("I cannot identify this string; please try again.")
            # print(len(compString))

        # if mystr evaluates to True as long as mystr is not empty; using that in the comparison to guard against empty strings and push that case into the else block
            if compString == compString[::-1] and compString:
                print(f"Yes! {palInput} is a palindrome; congratulations!")
            elif compString != compString[::-1] and compString:
                print(
                    f"I'm sorry; {palInput} is not a palindrome. Please try again.")
            else:
                print("I cannot identify this string; please try again.")


palCheck()
