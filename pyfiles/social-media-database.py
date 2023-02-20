#!/usr/bin/env python
import sqlite3

connection = sqlite3.connect('../database/social-network-database.db')
cursor = connection.cursor()

def addUser(username,userPassword,email):
    # Get the latest id
    cursor.execute("SELECT MAX(user_id) FROM user")
    maxID = cursor.fetchone()[0]
    if maxID is not None:
        userID = maxID + 1
    else:
        userID = 1

    userID = 0
    cursor.execute("""
    INSERT INTO user (user_id, username, user_password, email)
    VALUES(?,?,?,?)
    """,(userID, username, userPassword, email))
    connection.commit()

