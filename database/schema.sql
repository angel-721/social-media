CREATE TABLE users(
    user_id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    user_password TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

CREATE TABLE follows(
    user_id INTEGER,
    follower_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users (user_id),
    FOREIGN KEY (follower_id) REFERENCES users (user_id)
);

CREATE TABLE posts(
    post_id INTEGER PRIMARY KEY,
    poster_id INTEGER,
    content TEXT,
    created_time TIMESTAMP,
    FOREIGN KEY (poster_id) REFERENCES users (user_id)
);

CREATE TABLE likes(
    post_id INTEGER,
    liker_id INTEGER,
    PRIMARY KEY (post_id, liker_id),
    FOREIGN KEY (post_id) REFERENCES posts (post_id),
    FOREIGN KEY (liker_id) REFERENCES users (user_id)
);
