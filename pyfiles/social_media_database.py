#!/usr/bin/env python
import sqlite3


def addUser(userName,userPassword,email):
    connection = sqlite3.connect('../database/database.db')
    cursor = connection.cursor()
    # Get the latest id
    cursor.execute("SELECT MAX(user_id) FROM users")
    maxID = cursor.fetchone()[0]
    if maxID is not None:
        userID = maxID + 1
    else:
        userID = 1

    cursor.execute("""
    INSERT INTO users (user_id, username, user_password, email)
    VALUES(?,?,?,?)
    """,(userID, userName, userPassword, email))
    connection.commit()
    connection.close()

def deleteUser(userName):
    connection = sqlite3.connect('../database/database.db')
    cursor = connection.cursor()
    cursor.execute("""
    DELETE FROM users
    WHERE username == ?
    """,(userName,))
    connection.commit()
    connection.close()
    return

def followUser():
    return

def post():
    return

def unfollowUser():
    return

def likePost():
    return

def getFeed():
    return
