-- Cleanup existing DB
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS experience;
DROP TABLE IF EXISTS education;

-- Create tables
CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
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

-- Yes, I'm aware this is a terrible data model... will make this more dynamic/flexible in an admin UI
CREATE TABLE experience (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  name TEXT UNIQUE NOT NULL,
  title TEXT NOT NULL,
  location TEXT NOT NULL,
  dates TEXT NOT NULL,
  body TEXT NOT NULL
);

CREATE TABLE education (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  name TEXT UNIQUE NOT NULL,
  location TEXT NOT NULL,
  dates TEXT NOT NULL,
  body TEXT NOT NULL
);

-- Create some static data
INSERT INTO user (username, password)
VALUES
       ('mbryan', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f');

INSERT INTO post (title, body, author_id, created)
VALUES
       ('Welcome!', 'Thank you for visiting my blog. I hope to make this a central place to share my experiences and insights working in software.', 1, '2021-01-01 00:00:00'),
       ('Currently Working On: Crafting Interpreters', 'I''m currently working through Bob Nystrom''s Crafting Interpreters (http://www.craftinginterpreters.com/)', 1, '2021-01-20 00:00:00');

INSERT INTO experience (name, title, location, dates, body)
VALUES
       ('Broadway Technology', 'Senior Software Consultant', 'New York, NY', 'July 2018 - Present', 'Designing, building, and deploying mission-critical fintech solutions to satisfy complex client requirements.|Managed requirements gathering, design phases, and implementation of high-impact projects to deliver value to client businesses.|Identified and implemented enhancements to Broadway''s core products wherever possible when delivering solutions to clients.|Worked with clients on a daily basis to ensure customer success and communicate deliverable timelines.|Gained experience in Fixed Income and Crypto trading technologies.'),
       ('Yelp, Inc.', 'Software Engineer Intern', 'San Francisco, CA', 'May 2017 - August 2017', 'Improved data documentation service and data warehouse reporting as a member of Yelp''s Consumer Analytics and Metrics team.|Developed backend infrastructure for collecting, cleaning, and analyzing usage data for Yelp''s data warehouse and implemented frontend visualizations to describe and convey information to data warehouse administrators.|Provided insight into how Yelp engineers query the data warehouse, guiding decisions to improve system performance.|Redesigned React user interface for data documentation service in order to improve developer workflow.|Collaborated with engineers from a variety of teams in order to accomplish project goals.'),
       ('Toast, Inc.', 'Software Engineer Intern', 'Boston, MA', 'June 2016 - August 2016', 'Improved database layer of Toast''s core web application by refactoring the way developers write and release changes to data sources, increasing the reliability of deploying database schema migrations in both development and production environments and improving the efficiency of the engineering team.|Presented new development workflow to 40+ member engineering team and developed tooling and documentation to facilitate the transition to the new schema migration process.');

INSERT INTO education (name, location, dates, body)
VALUES
       ('Cornell University, College of Engineering', 'Ithaca, NY', 'May 2018', 'Bachelor''s Degree, Computer Science|Dyson Business Minor for Engineers|College of Engineering Dean''s List (Fall 2014, Fall 2016, Spring 2017)');
