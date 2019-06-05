# This is the AttemptsExceeded file to execute Zendesk code challenge
# This file is responsible for displaying error mesage and closing he program
# when user makes 3 incorrect attempts for any input
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


# Method to check the total number of incorrect attempts made by uesr
def InvalidAttempts(counter):
    if counter == 3:
        # Clear the screem
        clear()
        # Display error message
        print("You have exceeded maximum number of attempts."
              "\nClosing the application...")
        # Sleep for 2 seconds before closing the application
        sleep(2)
        # Close the application
        quit()
