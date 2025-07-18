-- This script updates the score of all records with name 'Bob' to 10
-- It handles cases with zero, one, or multiple Bob records
-- It doesn't use Bob's id value, only the name field
-- SQL keywords are in uppercase as required

UPDATE second_table
SET score = 10
WHERE name = 'Bob';
