#!/usr/bin/env python
import getpass
import datetime

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
    return userName, followName

def makePost():
    userName = input("What is your name? ")
    postContent = input("Post here: ")
    timeStamp = datetime.datetime.now()
    return userName, postContent, timeStamp
