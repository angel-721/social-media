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

def feed():
    userName = input("What is your name? ")
    numberPosts = input("Integer of posts you want to see: ")
    return userName, numberPosts

def baconFeed():
    userName = input("What is your name? ")
    numberPosts = int(input("Integer of posts you want to see: "))
    baconNumber = int(input("Max recommend number: "))
    return userName, baconNumber, numberPosts
