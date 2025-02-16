-- Write a query that prints a list of employee names (i.e.: the name attribute) for employees in Employee having a salary greater than  per month who have been employees for less than  months. Sort your result by ascending employee_id.

-- Input Format

-- The Employee table containing employee data for a company is described as follows:

/*
Enter your query here.
*/
SELECT name FROM EMPLOYEE
WHERE salary > 2000 AND months < 10
ORDER BY employee_id ASC;