DROP TABLE IF EXISTS movies;

CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255),
    year INT,
    duration INT
);


-- INSERT INTO crew (name) VALUES ('James T. Kirk');
-- INSERT INTO crew (name) VALUES ('Bones');
-- INSERT INTO crew (name) VALUES ('Spock');
-- INSERT INTO crew (name) VALUES ('Uhura');

-- INSERT INTO crew (name) VALUES ('Jean Luc Picard');
-- INSERT INTO crew (name) VALUES ('William Riker');
-- INSERT INTO crew (name) VALUES ('Deanna Troi');
-- INSERT INTO crew (name) VALUES ('Beverly Crusher');

-- INSERT INTO crew (name) VALUES ('Kathryn Janeway');
-- INSERT INTO crew (name) VALUES ('Chakotay');
-- INSERT INTO crew (name) VALUES ('Seven Of Five');
-- INSERT INTO crew (name) VALUES ('Tom Paris');


INSERT INTO movies (description, year, duration) 
VALUES ('The Motion Picture', 1979, 132);

INSERT INTO movies (description, year, duration) 
VALUES ('The Wrath Of Khan', 1982, 113);

INSERT INTO movies (description, year, duration) 
VALUES ('The Search For Spock', 1986, 119);

INSERT INTO movies (description, year, duration) 
VALUES ('Generations', 1994, 118);


--  1.  Return ALL the data in the 'movies' table. 
SELECT * FROM movies;

-- 2.  Return ONLY the name column from the 'crew' table
SELECT name FROM crew;

-- 3.  Oops! Someone spelled 'Seven of Nine's' name wrong! Change it to reflect the proper spelling.
UPDATE crew SET name ='Seven Of Nine' WHERE name = 'Seven of Fife';

 -- 4.  Return ONLY William Riker's name from the 'crew' table.
SELECT name FROM crew WHERE name = 'William Riker';

 -- 5.  The cinema has just heard that they will be holding an exclusive midnight showing of 'Resurrection'!! Create a new entry in the 'movies' table to reflect this.
INSERT INTO movies (description, year, duration) VALUES ('Resurrection', 1998, 103);

--  6.  Chakotay has decided to hijack our crew dinner, Remove him from the table of people.
DELETE FROM crew WHERE name = 'Chakotay';