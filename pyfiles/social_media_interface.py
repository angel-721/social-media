#!/usr/bin/env python
import getpass

def newUser():
    userName = input("Username: ")
    userEmail = input("Email: ")
    userPassword = getpass.getpass("Password: ")
    return userName, userEmail, userPassword

def getUserToDelete():
    userName = input("Username you want to delete: ")
    return userName

def follow():
    userName = input("What is your name? ")
    followName = input("Username of person to follow: ")
