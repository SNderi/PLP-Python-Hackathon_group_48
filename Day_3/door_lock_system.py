# -*- coding: utf-8 -*-
""" Module to simulate a door lock system """

from datetime import datetime
import calendar

# Password is set and stored in a variable
user_set_password = input("Set your password: ")  # "samplepwd"

# authenticated = True
door_open = False


# Define a function to control authentication
def authenticate(user_set_pwd, input_pwd):
    if user_set_pwd == input_pwd:
        return True
    else:
        return False


authenticated = authenticate(user_set_password, input("Enter your password: "))

while not authenticated:
    print("Wrong password")
    authenticated = authenticate(user_set_password, input("Enter your password: "))

print("Welcome")

if door_open:
    door_status = "open"
    print("The door is open")
else:
    door_status = "closed"
    print("The door is closed")


# opened_now = datetime.now()


def open_door(status):  # Status argument will take in the variable door_status
    global door_open
    global opened_now
    if status:
        return "The door is already open!"
    elif not status:
        door_open = True
        opened_now = datetime.now()
        return "The door is now open!"
    else:
        return "Invalid entry"


def close_door(status):  # Status argument will take in the variable door_status
    global door_open
    if not status:
        return "The door is already closed"
    elif status:
        door_open = False
        return "The door is now closed"
    else:
        return "Invalid entry"


time_of_open = "Never"
quit_operation = False
while not quit_operation:
    command = input("What is the command? open, close or quit? ")
    if command.lower() == "open":
        print(open_door(door_open))
        door_open = True
        # opened_now = datetime.now()
        time_of_open = opened_now.strftime("%m/%d/%Y %H:%M:%S.%f")
        print("Door last opened: ", time_of_open)
    elif command == "close":
        print(close_door(door_open))
        print("Door last opened: ", time_of_open)
        door_open = False
    elif command == "quit":
        print("Door last opened: ", time_of_open)
        print("Good Bye!")
        quit_operation = True
    else:
        print("Invalid Entry. Try again.")
        print("Door last opened: ", time_of_open)
