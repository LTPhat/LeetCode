-- Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.
-- The STATION table is described as follows:

/*
Enter your query here.
*/

SELECT DISTINCT CITY FROM STATION
WHERE ID % 2 = 0;
