# This is the MenuDisplay file to execute Zendesk code challenge
# This file contains all the display methods for all the menus in application
# This project was created for Student internship at Zendesk
# Created by: Abhishek Pahuja
# Email ID: abhishekpahuja@hotmail.com
# Created on: 5 June 2019
# Interpreter: Python 3.7.3

# Add all the files and methods
# import clear from user defined ClearScreen.py
from ClearScreen import clear
# Import sleep method from time to add delay wherever necessary
from time import sleep
# Import invalid attempts method to check if user has exceeded number of permitted attempts
from AttemptsExceeded import InvalidAttempts


# First menu to ask if user wants to start the application
def FirstMenu():
    # initialize the counter
    counter = 0
    # While loop to check the number of invalid attempts by the user
    while counter < 3:
        # Print the welcome message
        print("****** Welcome to Zendesk Ticket Viewer ******")
        # Display the menu
        # Get user input
        start = input("Please type S to start or Q to quit: ")
        if start.upper() == 'Q':
            print("Closing the program...")
            # Sleep for 2 seconds before closing the application
            sleep(2)
            # Set counter to 4 in order to quit the while loop
            counter = 4
            # Return false to close the program
            quit()
        elif start.upper() == 'S':
            # return True to start next loop
            return True
            # Set counter to 4 in order to quit the while loop
            counter = 4
            clear()
        else:
            # Increment the counter if no option matches
            counter += 1
            clear()
            # Display Error message
            print("Invalid Input. Please try again."
                  "\nAttempts remaining: " + str(3 - counter))

    # If the user made 3 invalid attempts, close the program.
    InvalidAttempts(counter)


# SecondMenu is responsible for asking user's choice of login
def SecondMenu():
    # initialise counter
    counter = 0
    # While loop to keep the incorrect attempts in check
    while counter < 3:
        clear()
        # Display the menu
        # Get user input
        print("Select option 1 to auto login using a test account"
              "\nSelect option 2 to enter your log in details"
              "\nSelect option 3 to close the application")
        option = input("Enter your choice: ")
        # Try block to catch input type mismatch
        try:
            choice = int(option)
            if choice == 1:     # User selects auto login
                # Set counter to 4 in order to quit the while loop
                counter = 4
                # Return true if user selects Auto login
                return True
            elif choice == 2:   # User Selects manual login
                # Set counter to 4 in order to quit the while loop
                counter = 4
                # Return false if user selects manual login
                return False
            elif choice == 3:   # user wants to close the application
                # Set counter to 4 in order to quit the while loop
                counter = 4
                quit()
            else:
                # If user's choice is out of range
                # increment the counter
                counter += 1
                # Display Error message
                print("Invalid value. Please select one option out of 1, 2 and 3"
                      "\nAttempts remaining: " + str(3 - counter))
        # Except block to catch value Error (if input is different that required data type)
        except ValueError:
            # Increment the counter
            counter += 1
            # Print error message for the user
            print("Invalid value. Please select one option out of 1, 2 and 3"
                  "\nAttempts remaining: " + str(3 - counter))
            # Sleep for 2 seconds before clearing the screen
            sleep(2)
            clear()

    # If the user made 3 invalid attempts, close the program.
    InvalidAttempts(counter)


# ThirdMenu is responsible for asking user's preferences once the user has logged in successfully
def ThirdMenu():
    # Initialise the counter
    counter = 0
    while counter < 3:
        # Display the menu
        option = input("Please select one of the following options:"
                       "\n\tSelect option 1 to display all the tickets"
                       "\n\tSelect option 2 to display a specific ticket"
                       "\n\tSelect option 3 to logout and try again"
                       "\n\tSelect option 4 to close the application."
                       "\n\tYour Choice: ")
        # Try block to catch input type mismatch
        try:
            choice = int(option)
            if choice == 1:     # User wants to display all the tickets
                clear()
                # Set counter to 4 in order to quit the while loop
                counter = 4
                return choice
            elif choice == 2:   # User wants to Select a specific ticket number
                # Set counter to 4 in order to quit the while loop
                counter = 4
                return choice
            elif choice == 3:   # User wants to try using another account/domain
                clear()
                # Set counter to 4 in order to quit the while loop
                counter = 4
                print("Logging out...")
                # Sleep for 2 seconds before clearing screen
                sleep(2)
                clear()
                return choice
            elif choice == 4:   # User wants to close the application
                clear()
                counter = 4
                print("Closing the application...")
                # Sleep for 2 seconds before closing the application
                sleep(2)
                quit()
            else:               # user has entered out of range option
                clear()
                # Increment the counter
                counter += 1
                # Display the error message
                print("Invalid choice. Please try again"
                      "\nAttempts remaining: " + str(3 - counter))
        # Except block to catch value Error (if input is different that required data type)
        except ValueError:
            # Increment the counter
            counter += 1
            # Display te error message
            print("Invalid value. Please select one option out of 1, 2, 3 and 4"
                  "\nAttempts remaining: " + str(3 - counter))
            # Add 2 second delay before clearing the screen
            sleep(2)
            clear()

    # If the user made 3 invalid attempts, close the program.
    InvalidAttempts(counter)

