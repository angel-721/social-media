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
    parser.add_argument("--TEST-add-posts", type=int, default=0)
    args = parser.parse_args()
    return args



def main(args):

    #testing stuff
    if(args.TEST_add_user != 0):
        #userName = getUserToDelete()
        file=open("testing_Addition.txt")
        for line in file:
            line2=line.split(',')
            #addUser(userName,userEmail,userPassword)
            addUser(line2[0],line2[1],line2[2])
        file.close()
    
    if(args.TEST_add_post != 0):
            file=open("../text_files/testing_add_posts.txt")
            for line in file:
                line=line.strip()
                line2=line.split('-,-')
                #addPost(line2[0],line2[1]);
            file.close()
    if(args.TEST_add_post != 0):
            file=open("../text_files/testing_following.txt")
            for line in file:
                line=line.strip()
                line2=line.split(',')
                for bit in line2:
                    bit.strip()
                #follow(line2[0],line2[1]);
            file.close()

    if(args.TEST_delete_user != 0):
        file=open("../text_files/testing_Addition.txt")
        for line in file:
            line2=line.split(',')
            #addUser(userName,userEmail,userPassword)
            addUser(line2[0],line2[1],line2[2])
        file.close()
        file3=open("../text_files/testing_Delete.txt")
        #userName = getUserToDelete()
        for line in file3:
            line=line.strip()
            deleteUser(line)
        file3.close()
    #delete shoulld be the last one cause it'll mess up the others if it stays.


    if(args.add_user != 0):
        userName, userEmail, userPassword = newUser()
        addUser(userName,userEmail,userPassword)
    if(args.delete_user != 0):
        userName = getUserToDelete()
        deleteUser(userName)
    


if __name__ == "__main__":
    main(parseArgs())

