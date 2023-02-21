#!/usr/bin/env python
import getpass

def newUser():
    userName = input("Username:: ")
    userEmail = input("Email: ")
    userPassword = getpass.getpass("Password: ")
    return userName, userEmail, userPassword

def getUserToDelete():
    userName = input("Username you want to delete: ")
    return userName
