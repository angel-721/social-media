#!/usr/bin/env python
import sqlite3


def addUser(userName,userPassword,email):
    connection = sqlite3.connect('../database/database.db')
    cursor = connection.cursor()

    try:
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
        print("Added", userName)
    except:
        print("Users Table Does not exist")
    finally:
        connection.close()
    return

def deleteUser(userName):
    connection = sqlite3.connect('../database/database.db')
    cursor = connection.cursor()
    try:
        cursor.execute("""
        DELETE FROM users
        WHERE username == ?
        """,(userName,))
        connection.commit()
        print(userName, "Deleted")
    except:
        "Can not delete User"
    finally:
        connection.close()
    return
"""
FIX LATER
SO I messed up and followerName is the user that is getting Followed
and UserName is the user that is following the follower
It's a trip.
"""
def followUser(userName, followerName):
    connection = sqlite3.connect('../database/database.db')
    cursor = connection.cursor()

    try:
        table = cursor.execute("""
        SELECT user_id FROM users WHERE username = ?;
        """,(userName,)).fetchall()
        userID = table[0][0]
    except:
        print(userName, "Does not exist")

    try:
        table = cursor.execute("""
        SELECT user_id FROM users WHERE username = ?;
        """,(followerName,)).fetchall()
        followerID = table[0][0]
    except:
        print(userName, "Does not exist")

    cursor.execute("""
    INSERT INTO follows (user_id, follower_id)
    VALUES(?,?);
    """,(followerID, userID))
    connection.commit()
    connection.close()
    print(userName, "Followed", followerName)
    return

def post(userName, postContent, timeStamp):
    connection = sqlite3.connect('../database/database.db')
    cursor = connection.cursor()

    cursor.execute("SELECT MAX(post_id) FROM posts")
    maxID = cursor.fetchone()[0]
    if maxID is not None:
        postID = maxID + 1
    else:
        postID = 1

    table = cursor.execute("""
    SELECT user_id FROM users WHERE username = ?;
    """,(userName,)).fetchall()
    userID = table[0][0]


    cursor.execute("""
    INSERT INTO posts (post_id, poster_id, content, created_time)
    VALUES(?,?,?,?);
    """,(postID, userID, postContent, timeStamp))

    connection.commit()
    connection.close()
    print(userName, "posted", postContent, "on\n", timeStamp)
    return


def getFeed(userName,numberPosts):
    connection = sqlite3.connect('../database/database.db')
    cursor = connection.cursor()

    table = cursor.execute("""
    SELECT user_id FROM users WHERE username = ?;
    """,(userName,)).fetchall()
    userID = table[0][0]

    feed = cursor.execute("""
    SELECT posts.content, posts.created_time, poster.username
    FROM users AS follower
    JOIN follows ON follower.user_id = follows.follower_id
    JOIN users AS poster ON follows.user_id = poster.user_id
    JOIN posts ON posts.poster_id = poster.user_id
    WHERE follower.user_id = ?;
    """,(userID,)).fetchall()
    userFeed = []
    if len(feed) <= numberPosts:
        numberPosts = len(feed)

    for i in range(numberPosts):
        userFeed.append(feed[i])
    print(userFeed)

    print("------FEED-----")
    for i in userFeed:
        print(i[2], "- \n", i[0], "\n on", i[1])
        print()

    connection.commit()
    connection.close()
    return

def dummyusers():
    return
