#!/usr/bin/env python
from social_media_database import *
from social_media_interface import *
import argparse

def parseArgs():
    parser = argparse.ArgumentParser(prog="Social Media", description="A simple command line social media")
    parser.add_argument("--add-user", type=int, default=0)
    parser.add_argument("--delete-user", type=int, default=0)
    args = parser.parse_args()
    return args

def main(args):
    if(args.add_user != 0):
        userName, userEmail, userPassword = newUser()
        addUser(userName,userEmail,userPassword)
    if(args.delete_user != 0):
        userName = getUserToDelete()
        deleteUser(userName)


if __name__ == "__main__":
    main(parseArgs())