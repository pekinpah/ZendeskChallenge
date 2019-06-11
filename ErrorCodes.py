# This is the ErrorCOdes file to execute Zendesk code challenge
# This file is displaying the type of error and provide a link for more information to the user
# This project was created for Student internship at Zendesk
# Created by: Abhishek Pahuja
# Email ID: abhishekpahuja@hotmail.com
# Created on: 11 June 2019
# Interpreter: Python 3.7.3


def ErrorCodes(Code):
    # Client Error Response codes
    if Code >= 400 and Code < 452:
        print("Client Side Error. Status Code: " + str(Code) +
              "\nFor more details visit: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status")
    # Server Side Error Codes
    elif Code >= 500 and Code <512:
        print("Server Side Error. Status Code: " + str(Code) +
              "\nFor more details visit: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status")
    # Anything out of range
    else:
        print("Error Code not defined")
