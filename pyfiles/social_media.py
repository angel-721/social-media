#!/usr/bin/env python
from social_media_database import *
from social_media_interface import *
import argparse

def parseArgs():
    parser = argparse.ArgumentParser(prog="Social Media", description="A simple command line social media")
    parser.add_argument("--add-user", type=int, default=0)
    parser.add_argument("--delete-user", type=int, default=0)
    parser.add_argument("--TEST-add-user", type=int, default=0)
    parser.add_argument("--TEST-delete-user", type=int, default=0)
    parser.add_argument("--follow-user", type=int, default=0)

    args = parser.parse_args()
    return args



def main(args):
    if(args.add_user != 0):
        userName, userEmail, userPassword = newUser()
        addUser(userName,userEmail,userPassword)
    if(args.delete_user != 0):
        userName = getUserToDelete()
        deleteUser(userName)
    if(args.follow_user != 0):
        userName, followName = follow()
        followUser(userName, followName)
    if(args.TEST_add_user != 0):
        userName = getUserToDelete()
        file=file.open("testing_Addition.txt")
        for line in file:
            line2=line.split(',')
            #addUser(userName,userEmail,userPassword)
            addUser(line2[0],line2[1],line2[2])
    if(args.TEST_delete_user != 0):
        file=file.open("testing_Delete.txt")
        #userName = getUserToDelete()
        for line in file:
            line=line.strip()
            deleteUser(line)


if __name__ == "__main__":
    main(parseArgs())

