# This is the main file to execute the Zendesk code challenge
# This file connects all the methods defined in other files
# This project was created for Student internship at Zendesk
# Created by: Abhishek Pahuja
# Email ID: abhishekpahuja@hotmail.com
# Created on: 5 June 2019
# Interpreter: Python 3.7.3

# Add all the files and methods
# From MenuDisplay, import all the menus
from MenuDisplay import FirstMenu
from MenuDisplay import SecondMenu
from MenuDisplay import ThirdMenu
# From getlogin import both login methods
from GetLogin import Login
from GetLogin import AutoLogin
# From dataDisplay import both the display choices
from DataDisplay import DisplayAll
from DataDisplay import DisplaySelected


# Infinite while loop
while True:
    start = False
    # call the first menu method to display first menu
    start = FirstMenu()
    # Boolean value to determine if user wants to continue
    if start:
        Logout = False
        # Ask user to select log in type
        LoginType = SecondMenu()
        if LoginType:
            # For test account
            DataArray = AutoLogin()
        elif not LoginType:
            # For user defined account
            DataArray = Login()

        # Program will continue if the entered credentials are correct.
        while not Logout:
            # Menu to display tickets
            choice = ThirdMenu()
            if choice == 1:
                # Method to Display all the tickets
                DisplayAll(DataArray)
            elif choice == 2:
                # Method to Display ticket number defined by user
                DisplaySelected(DataArray)
            elif choice == 3:
                # This will ask the user for selecting domain and user credentials
                # for a new account
                Logout = True
