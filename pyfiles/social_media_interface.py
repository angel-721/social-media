#!/usr/bin/env python
import getpass

def newUser():
    userName = input("Name: ")
    userEmail = input("Email: ")
    userPassword = getpass.getpass("Password: ")
    return userName, userEmail, userPassword
