-- Script that lists all the records of the table with some specifications.
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
