-- Cleanup existing DB
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

-- Create tables
CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  fullname TEXT NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

-- Create some static data
INSERT INTO user (username, fullname, password)
VALUES
       ('mbryan', 'Mark Bryan', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f');

INSERT INTO post (title, body, author_id, created)
VALUES
       ('Welcome!', 'Thank you for visiting my blog. I hope to make this a central place to share my experiences and insights working in software.', 1, '2021-01-01 00:00:00'),
       ('Currently Working On: Crafting Interpreters', 'I''m currently working through Bob Nystrom''s Crafting Interpreters (http://www.craftinginterpreters.com/)', 1, '2021-01-20 00:00:00');
