# This is the GetLogin file to execute Zendesk code challenge
# This file is responsible for connecting to Zendesk API and getting the ticket data for the user
# This project was created for Student internship at Zendesk
# Created by: Abhishek Pahuja
# Email ID: abhishekpahuja@hotmail.com
# Created on: 5 June 2019
# Interpreter: Python 3.7.3

# Add all the files and methods
# Import requests to send and receive requests
import requests
# time.sleep method to add delays wherever required
from time import sleep
# import clear from user defined ClearScreen.py
from ClearScreen import clear
# Import getpass from getpass to read passwords
from getpass import getpass
# Import base 64 to decode test account credentials
import base64
# Import invalid attempts method to check if user has exceeded number of permitted attempts
from AttemptsExceeded import InvalidAttempts
# import the ErrorCodes method from ErrorCodes.py
from ErrorCodes import ErrorCodes

# Login method to allow user to log into their account and domain
def Login():
    # Set counter to 0
    counter = 0
    # If user does not make 3 incorrect attempts continue
    while counter < 3:
        print('https://{DomainName}.zendesk.com')
        # Get user's login details
        domain = input("Please enter the domain name (without curly braces): ")
        email = input("Please enter your email address: ")
        password = getpass("Please enter your password: ")
        credentials = email, password
        # Create session
        session = requests.Session()
        # Authenticate user
        session.auth = credentials
        zendesk = 'https://' + domain + '.zendesk.com/api/v2/tickets.json?page='
        url = zendesk + '1'
        # Get response from the Zendesk server
        response = session.get(url)
        # Check if the response was received
        if response.status_code != 200:
            # Call the error code method from errorCode.py
            ErrorCodes(response.status_code)
            # Sleep for 5 seconds before clearing screen
            sleep(5)
            clear()
            # Increment the counter
            counter += 1
            clear()
            print("Please check the data you entered."
                  "\nDomain Name: " + domain +
                  "\nEmail ID: " + email +
                  "\nPassword: " + password +
                  "\nTotal attempts remaining: " + str(3-counter))
        else:
            clear()
            # Check the number of pages
            DATA = response.json()
            total_records = DATA['count']
            # Calculate the number of pages
            Total_Pages = int(total_records / 100) + 1
            # If more than 1 page(100 tickets)
            DataArray = [DATA]*(total_records)
            RecordArray = [DATA] * Total_Pages
            PageCount = 1
            recordcounter = 0
            # Put all the data in arrays
            while recordcounter < total_records:
                for records in RecordArray:
                    zendesk = 'https://' + domain + '.zendesk.com/api/v2/tickets.json?page='
                    url = zendesk + str(PageCount)
                    response = session.get(url)
                    # get all the ticket records
                    records = response.json()
                    # Get individual ticket records
                    for data in records['tickets']:
                        DataArray[recordcounter] = data
                        # Increment the record counter
                        recordcounter += 1
                    # Increment the to next page
                    PageCount += 1
            # Set counter to 4 to break while loop
            counter = 4
            # display a message if no tickets were found
            if total_records == 0:
                print('this account has zero tickets. requsting tickets dislay will result in blank output')
            # Return the ticket data
            return DataArray

    # If the user made 3 invalid attempts, close the program.
    InvalidAttempts(counter)


# AutoLogin method contains credentials for a test account
def AutoLogin():
    # Decode the credentials
    credentials = base64.b64decode(b'YWJoaXNoZWtwYWh1amFAaG90bWFpbC5jb20=').decode('utf-8'), base64.b64decode(b'UElSQVRFU29mVEhFY2FyaWJiZWFu').decode('utf-8')
    # Create session
    session = requests.Session()
    # Authenticate test user
    session.auth = credentials
    zendesk = 'https://thedottedline.zendesk.com/api/v2/tickets.json?page='
    url = zendesk + '1'
    response = session.get(url)
    if response.status_code != 200:
        # Call the error code method from errorCode.py
        ErrorCodes(response.status_code)
        # Sleep for 5 seconds before clearing screen
        sleep(5)
        clear()
    else:
        clear()
        # Check the number of pages
        DATA = response.json()
        total_records = DATA['count']
        # Calculate the number of pages
        Total_Pages = int(total_records / 100) + 1
        # If more than 1 page(100 tickets)
        DataArray = [DATA] * (total_records)
        RecordArray = [DATA] * Total_Pages

        # Initialise counters
        PageCount = 1
        recordcounter = 0
        # Put all the data in arrays
        while recordcounter < total_records:
            for records in RecordArray:
                zendesk = 'https://thedottedline.zendesk.com/api/v2/tickets.json?page='
                url = zendesk + str(PageCount)
                response = session.get(url)
                # Get all the ticket records
                records = response.json()
                # Get individual ticket records
                for data in records['tickets']:
                    DataArray[recordcounter] = data
                    # Increment the record counter
                    recordcounter += 1
                # Increment to next page
                PageCount += 1
        # display a message if no tickets were found
            if total_records == 0:
                print('this account has zero tickets. requsting tickets dislay will result in blank output')
        # Return the collected tickets
        return DataArray
