CREATE TABLE user(
    user_id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    user_password TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE follow(
    user_id INTEGER,
    follower_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES user (user_id),
    FOREIGN KEY (follower_id) REFERENCES user (user_id)
);

CREATE TABLE post(
    post_id INTEGER PRIMARY KEY,
    poster_id INTEGER,
    content TEXT,
    created_time TIMESTAMP,
    FOREIGN KEY (poster_id) REFERENCES user (user_id)
);

CREATE TABLE like(
    post_id INTEGER,
    liker_id INTEGER,
    PRIMARY KEY (post_id, liker_id),
    FOREIGN KEY (post_id) REFERENCES post (post_id)
    FOREIGN KEY (liker_id) REFERENCES user (user_id)
);
