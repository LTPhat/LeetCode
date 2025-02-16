-- Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.

-- Input Format

-- The STATION table is described as follows:

/*
Enter your query here.
*/

SELECT DISTINCT CITY FROM STATION
WHERE LEFT(CITY, 1) NOT IN ('a', 'e', 'i', 'o', 'u');