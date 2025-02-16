-- Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.

-- Input Format

-- The STATION table is described as follows:

/*
Enter your query here.
*/
SELECT DISTINCT CITY FROM STATION 
WHERE LEFT(CITY, 1) NOT IN ('a', 'e', 'i', 'u', 'o')
AND RIGHT(CITY, 1) NOT IN ('a', 'e', 'i', 'u', 'o');