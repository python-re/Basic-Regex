#----------------------------------------------------------------------------------------------------------------------------------------------------------
#

import sys
import time
import re

#
#----------------------------------------------------------------------------------------------------------------------------------------------------------
#

print("---------------------------------------------------------------------------------------------------------------------------------------------")

print("For more information on Regex, please visit my GitHub and look for some ReGex expressions you can use.")
print("Similarly, you can look up Regex sheets and experiment with that code. Regex is more useful than you, currently, might think.")

print("---------------------------------------------------------------------------------------------------------------------------------------------")

print("Welcome to the ReGex program. A little about the code before you go on so it's CRUCIAL you read this.")
print("Regex is a very crucial tool when we're looking for specific criterium in other people's code or files/documents")

print("---------------------------------------------------------------------------------------------------------------------------------------------")

print("Depending on your operating system, the file directory WILL matter. You will run into an error if it can't find the file on your computer.")
print("If it can't find the file, it will automatically terminate this program and you will have to re-run it.")

print("---------------------------------------------------------------------------------------------------------------------------------------------")

#
#----------------------------------------------------------------------------------------------------------------------------------------------------------
#

# Ask for the first directory. Currently, this program only supports complete document paths.
inputOne = input("Please provide the first file directory here: ")

# Give the user three attempts to input a correct response.
attempts = 1

# While the user still has attempts remaining; go through the while loop.
while (attempts < 4):

    print("---------------------------------------------------------------------------------------------------------------------------------------------")

    # [Optional]: Allow the user to utilize another file in the program.
    # It's my goal to allow the user to use up to THREE (3) files at some point in the future.

    print("You have the option of using another file directory.")
    print()

    # List how many attempts the user has.

    print("You are given three attempts. Afer three attempts, the program will auto-terminate. Attempts are logged below.")
    print("This is attempt " + str(attempts) + " out of 3.")
    print()

    # Await a user's input from the keyboard.

    confirmString = str(input("Would you like to use another directory? Please type (Yes) or (No): "))

#
#----------------------------------------------------------------------------------------------------------------------------------------------------------
#
    # Did the user type "YES," "yEs," or "YEs?" If so, take the confirmation string, format at it to all lowercase, and enter the if-statement.
    if (confirmString.lower() == "yes"):

        print("---------------------------------------------------------------------------------------------------------------------------------------------")

        # Confirm the user's inputted response.

        print("You chose \"yes.\"")

        # Supply a second directory. Once again, this program currently only supports complete file paths.
        inputTwo = input("Please type the second file directory here: ")
        print()

        # --------------------------------------------------------------------------------------------------------------------------------------------------------

        print("Opening the files... This may take a moment. Currently, if the program can't open your file, the program will terminate with an error.")
        print("[Next patch will introduce find handlers]")
        print()

        openPendingFileAttempts = 0
        openPendingFileString = "."

        # This will allow the user to keep track of how long the files take to open (five seconds so that lower-end operating systems don't crash).
        while (openPendingFileAttempts < 6):

            print(openPendingFileString, end = "")


            # Sleep for one second, before resuming
            time.sleep(1)
            openPendingFileAttempts += 1

        print('\n')

        # Open the first file (primary).
        primaryFile = open(inputOne, mode = "r", encoding = "utf-8", errors = "ignore")

        # Open the second file (secondary).
        secondaryFile = open(inputTwo, mode = "r", encoding = "utf-8", errors = "ignore")

        # Verify that the files opened successfully.
        print("Your files were opened successfully.")

        print("---------------------------------------------------------------------------------------------------------------------------------------------")

        # --------------------------------------------------------------------------------------------------------------------------------------------------------

        # Ask the user for a regex expression.
        regexExpressionMatch = str(input("What regex expression would you like to use [example: ^Hello, Hello$, H]? "))
        print("---------------------------------------------------------------------------------------------------------------------------------------------")

        # --------------------------------------------------------------------------------------------------------------------------------------------------------
        # Authenticate the files

        PendingOne = 0
        PendingOnePhrase = ('.')

        print("Authenticating Files", end = "")

        while (PendingOne <= 10):

            print(PendingOnePhrase, end = "")
            time.sleep(1)
            PendingOne += 1

        print('Check [0]', end = "")
        print()

        # --------------------------------------------------------------------------------------------------------------------------------------------------------
        # Load the regex statement and prepare it for use.

        PendingTwo = 0
        PendingTwoPhrase = ('.')

        print("Loading Regex Statement", end = "")

        while (PendingTwo <= 20):

            print(PendingTwoPhrase, end = "")
            time.sleep(0.5)
            PendingTwo += 1

        print('Check [0]', end = "")
        print()

        # --------------------------------------------------------------------------------------------------------------------------------------------------------
        # Verify the status of the system.

        PendingThree = 0
        PendingThreePhrase = ('.')

        print("Verifying System Status", end = "")

        while (PendingThree <= 80):

            print(PendingTwoPhrase, end="")
            time.sleep(0.1)
            PendingThree += 1

        print('Check [0]', end="")
        print()

        # --------------------------------------------------------------------------------------------------------------------------------------------------------

        print("---------------------------------------------------------------------------------------------------------------------------------------------")

        print("Program is ready... The options you have to choose from are as follows:")
        print()

        time.sleep(1)
        print("Value Deletion (A)" , end = "")

        time.sleep(1)
        print(" | Value Duplicating (B)" , end = "")

        time.sleep(1)
        print(" | Value Swapping (C)")

        print("---------------------------------------------------------------------------------------------------------------------------------------------")

        yourChoice = str(input("Please enter the letter associated with the choice you decide to go with: "))

        # TODO: 2/3 features are complete for the two file component.
        # TODO: Deletion and Duplication have been finalized.
        # TODO: Combination will most likely involve two regex statements.

        # --------------------------------------------------------------------------------------------------------------------------------------------------------
        # Deletion feature code for TWO files.

        if (yourChoice.lower() == "a"):

            print("You've selected \"Value Deletion.\" Please give the program a moment to delete words delete matching values.")
            print("---------------------------------------------------------------------------------------------------------------------------------------------")
            time.sleep(2)

            for line in primaryFile:

                if (re.search(regexExpressionMatch, line)):

                    line = ("[Line Deleted Successfully]")

                print()
                print("---------------------------------------------------------------------------------------------------------------------------------------------")

                print('[First File]')
                print(line, end = "")

            # --------------------------------------------------------------------------------------------------------------------------------------------------------

            for line in secondaryFile:

                if (re.search(regexExpressionMatch, line)):
                    line = ("[Line Deleted Successfully]")

                print()
                print("---------------------------------------------------------------------------------------------------------------------------------------------")

                print('[Second File]')
                print(line, end = "")

            print()
            print("---------------------------------------------------------------------------------------------------------------------------------------------")


        # --------------------------------------------------------------------------------------------------------------------------------------------------------
        # Duplication feature code for TWO files.

        if (yourChoice.lower() == "b"):
            print("You've selected \"Value Duplicating.\" Please give the program a moment to repeat matching values, once.")
            print("---------------------------------------------------------------------------------------------------------------------------------------------")

            time.sleep(2)

            for line in primaryFile:

                if (re.search(regexExpressionMatch, line)):

                    line = (line.rstrip('\n') + " " + line)

                print('[First File]')
                print(line, end= "")

                print("---------------------------------------------------------------------------------------------------------------------------------------------")

            print()

            # --------------------------------------------------------------------------------------------------------------------------------------------------------

            for line in secondaryFile:

                if (re.search(regexExpressionMatch, line)):

                    line = (line.rstrip('\n') + " " + line)

                print("---------------------------------------------------------------------------------------------------------------------------------------------")

                print('[Second File]')
                print(line, end = "")

            print()
            print("---------------------------------------------------------------------------------------------------------------------------------------------")

            # --------------------------------------------------------------------------------------------------------------------------------------------------------

        # TODO Start combination code here.

        if (yourChoice.lower() == "c"):

            print("You've selected \"Swapping Values.\" The program will now swap the first and last indices.")
            print("---------------------------------------------------------------------------------------------------------------------------------------------")


            for line in primaryFile:

                if (re.search(regexExpressionMatch, line)):

                    lineSwapOne = line
                    lineSwapTwo = line[::-1]

                    line = line.replace(lineSwapOne[0], lineSwapTwo[1])

                    print(line)

                    # print(lineSwapOne[0]) // First letter of each word.
                    # print(lineSwapTwo[1]) // Last letter of each word.







        break


#
# ----------------------------------------------------------------------------------------------------------------------------------------------------------
#

# TODO If the user is to input "no," expected behavior should be almost equal to the above code.
# TODO However, instead of dealing with two files, we'll only worry about one. Copying and pasting the above
# TODO code is the best way about going about this as you'll be able to better control bugs and errors that may
# TODO come up.

    if (confirmString.lower() == "no"):

        print("That's ok! It was just an option, and I respect your decision.")
        print()

        print("Let's go ahead and open that file for you. Please wait...")

        time.sleep(2)

        primaryFile = open(inputOne, mode = "r", encoding = "utf-8", errors = "ignore")

        print("Success! Your file took " + str(time.time()) + " s/ms to open.")
        print()

        print("Let's continue!")

        break


# TODO This part of the code is finished and doesn't need any further testing.

    if (confirmString.lower() != "yes" or confirmString.lower() != "no" or confirmString.lower() == ""):

        attempts += 1

        if (attempts == 4):
            sys.exit("Number of attempts succeeded. Exiting program.")

        else:
            print("---------------------------------------------------------------------------------------------------------------------------------------------")

            print("You've supplied an invalid response of: " + "\"" + confirmString + "\"")
            print("Reformatting...")

            time.sleep(1)
