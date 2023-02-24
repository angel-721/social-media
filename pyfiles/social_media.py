#!/usr/bin/env python
from social_media_database import *
from social_media_interface import *
import argparse

def parseArgs():
    parser = argparse.ArgumentParser(prog="Social Media", description="A simple command line social media")
    parser.add_argument("--add-user", type=int, default=0)
    parser.add_argument("--delete-user", type=int, default=0)
    parser.add_argument("--follow-user", type=int, default=0)
    parser.add_argument("--post", type=int, default=0)
    parser.add_argument("--feed", type=int, default=0)
    parser.add_argument("--bacon-feed", type=int, default=0)

    #the tests
    parser.add_argument("--TEST-add-user", type=int, default=0)
    parser.add_argument("--TEST-delete-user", type=int, default=0)
    parser.add_argument("--TEST-add-post", type=int, default=0)
    parser.add_argument("--TEST-following", type=int, default=0)

    args = parser.parse_args()
    return args



def main(args):

    #testing stuff
    if(args.TEST_add_user != 0):
        #userName = getUserToDelete()
        file=open("../text_files/testing_Addition.txt")
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
    if(args.TEST_following != 0):
            file=open("../text_files/testing_following.txt")
            for line in file:
                line=line.strip()
                line2=line.split(',')
                for bit in line2:
                    bit.strip()
                #follow(line2[0],line2[1]);
            file.close()

    if(args.TEST_delete_user != 0):
        if(args.TEST_add_user == 0):
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
    if(args.follow_user != 0):
        userName, followName = follow()
        followUser(userName, followName)
    if(args.post != 0):
        userName, postContent, timeStamp = makePost()
        post(userName, postContent, timeStamp)
    if(args.feed != 0):
        userName,numberPosts = feed()
        getFeed(userName,int(numberPosts))
    if(args.bacon_feed != 0):
        userName,numberPosts,baconNumber = baconFeed()
        getBaconFeed(userName,baconNumber,numberPosts)

if __name__ == "__main__":
    main(parseArgs())

