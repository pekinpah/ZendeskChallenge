# ZendeskChallenge
Repository for Zendesk Coding Challenge - June 2019
# About the Project
Developed by: Abhishek Pahuja

Application Type: Console Application

Email ID: abhishekpahuja@hotmail.com

Date: 5 June 2019

Purpose: Zendesk Student Internship - Coding Challenge

IDE Used: pyCharm Community edition

Download Here: [pyCharm](https://www.jetbrains.com/pycharm/download/)

Main File name: Zendesk_Challenge_Main.py

Programming language Used: Python 3.7.3
Download Here: [Python Docs](https://www.python.org/downloads/release/python-373/)


## Requirements:

1. Install python 3.7.3 (or above) and add python to path

2. To update/upgrade pip type
```bash
python -m pip install --upgrade pip
```

3. Install the requests package using pip3
```bash
pip3 install requests
```
## Usage
1. To run the project, navigate to src directory/your project directory using terminal/command prompt and type this command:
```bash
python Zendesk_Challenge_Main.py
```

2. Follow the menu prompts.

## Tests
The code worked without any changes, however, there were type mismatch errors when non-numeric values were entered where numeric input was required. Try-except conditions were used to remove that error.

The program was tested for a test account using both the input methods. However, this program fetches 100 requests per page instead of 25 (as mentioned in the requirements sheet). Therefore, pagination is coded to handle 100 tickets per page instead of 25.
