-- Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.

-- Input Format

-- The STATION table is described as follows:

/*
Enter your query here.
*/
select distinct city from station where left(city,1) not in('a','e','i','o','u') or right(city,1) not in('a','e','i','o','u');