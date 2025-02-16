-- Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

-- Input Format

-- The STATION table is described as follows:

/*
Enter your query here.
*/

SELECT DISTINCT CITY FROM STATION
WHERE
CITY LIKE 'a%' or
CITY LIKE 'e%' or
CITY LIKE 'i%' or
CITY LIKE 'o%' or
CITY LIKE 'u%';
