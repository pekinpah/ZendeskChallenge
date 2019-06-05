# This is the ClearScreen file to execute Zendesk code challenge
# This file is responsible for connecting to Zendesk API and getting the ticket data for the user
# This project was created for Student internship at Zendesk
# The code in this file was tak from the following link
# https://www.geeksforgeeks.org/clear-screen-python/
# Interpreter: Python 3.7.3

# import only system from os
from os import system, name
# import sleep to provide a slight delay after clearing the screen
from time import sleep


# define the clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
    # sleep for 1 second to allow program to process data
    sleep(1)
