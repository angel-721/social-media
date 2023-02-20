#!/usr/bin/env python
from ./social-media-database.py import *
import argparse











def parseArgs():
    parser = argparse.ArgumentParser(prog="Social Media", description="A simple command line social media")
    # parser.add_argument("-login", type=str, required=True)
    args = parser.parse_args()
    return args

# testing to come soon!
def main(args):
    # if (args.deploy == "login"):
    #     login()

if __name__ == "__main__":
    main(parseArgs())
