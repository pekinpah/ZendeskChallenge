# This is the DataDisplay file to execute Zendesk code challenge
# This file is responsible for displaying the tickets as requested by the user
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

# This method will desplay all the tickets
def DisplayAll(DataArray):
    clear()
    print("\n\n")
    # For loop to get all the elements of the array to print the required data
    for ticket in DataArray:
        # Tabulate and separate all the tickets
        print("--------------------------------------------------------------------------")
        print('Ticket ID: {}'.format(ticket['id']))
        print("--------------------------------------------------------------------------")
        print("Ticket Subject: {}\n"
              "Ticket Status: {}\n"
              "Requester ID: {}\n"
              "Submitter ID: {}"
              .format(ticket['raw_subject'],
                      ticket['status'],
                      ticket['submitter_id'],
                      ticket['assignee_id']))
        print("--------------------------------------------------------------------------\n\n")


# This method will display the ticket defined by the user
def DisplaySelected(DataArray):
    clear()
    # Initialise the counters
    itemCounter = 0
    counter = 0
    for temp in DataArray:
        # counter to get the total number of tickets
        itemCounter += 1
    # While loop to limit number of attempts
    while counter < 3:
        option = input("Total tickets: " + str(itemCounter) +
                       "\nPlease enter the ticket ticket to be searched: ")
        # Try block to catch input type mismatch
        try:
            choice = int(option)
            if choice <= itemCounter and choice > 0:
                clear()
                for ticket in DataArray:
                    for id in ticket.values():
                        # If the id is fount in the tickets
                        # Print the required ticket
                        if id == choice:
                            # Tabulate and separate all the tickets
                            print("\n\n--------------------------------------------------------------------------")
                            print('Ticket ID: {}'.format(ticket['id']))
                            print("--------------------------------------------------------------------------")
                            print("Ticket Subject: {}\n"
                                  "Ticket Status: {}\n"
                                  "Requester ID: {}\n"
                                  "Submitter ID: {}\n"
                                  "Ticket Description: {}"
                                  .format(ticket['raw_subject'],
                                          ticket['status'],
                                          ticket['submitter_id'],
                                          ticket['assignee_id'],
                                          ticket['description']))
                            print("--------------------------------------------------------------------------\n\n")
                            # Set counter to 4 in order to quit the while loop
                            counter = 4
                            break
            # If the user entered out of range value
            elif choice > itemCounter or choice <= 0:
                # increment the attempt counter
                counter += 1
                # display error message
                print("The id you have entered is out of range. Please try again."
                      "\nYou selected: " + str(choice) +
                      "\nNumber of attempts remaining: " + str(3-counter))
        # Except block to catch value Error (if input is different that required data type)
        except ValueError:
            counter += 1
            print("Invalid value. Please select a valid value"
                  "\nAttempts remaining: " + str(3 - counter))
            # Sleep for 2 seconds before clearing screen
            sleep(2)
            clear()

    # If the user made 3 invalid attempts, close the program.
    InvalidAttempts(counter)
