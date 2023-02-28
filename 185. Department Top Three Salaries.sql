# Score
#  Runtime: 5%
#
# Description
#
# A company's executives are interested in seeing who earns the most money in each of the company's departments. A high earner in a department is an employee who has a salary in the top three unique salaries for that department.
#
# Write an SQL query to find the employees who are high earners in each of the departments.
#
# Return the result table in any order.
#
# The query result format is in the following example.
#

SELECT department.name AS Department, employee.name AS Employee, employee.salary AS Salary
FROM Employee employee
INNER JOIN Department department
ON employee.departmentId = department.id
WHERE CONCAT_WS('-', employee.departmentId, employee.salary) IN (
  SELECT CONCAT_WS('-', e2.departmentId, MAX(e2.salary))
  FROM Employee e2 GROUP BY e2.departmentId
  ORDER BY e2.salary DESC
) or CONCAT_WS('-', departmentId, salary) IN (
  SELECT CONCAT_WS('-', e3.departmentId, MAX(e3.salary))
  FROM (
    SELECT e4.salary, e4.departmentId
    FROM Employee e4
    WHERE CONCAT(e4.departmentId, e4.salary) NOT IN (
      SELECT CONCAT(e5.departmentId, MAX(e5.salary))
      FROM Employee e5
      GROUP BY departmentId
    )
  ) e3
  GROUP BY e3.departmentId
) or CONCAT_WS('-', employee.departmentId, employee.salary) IN (
  SELECT CONCAT_WS('-', e6.departmentId, MAX(e6.salary))
  FROM (
    SELECT e7.salary, e7.departmentId
    FROM Employee e7
    WHERE CONCAT(e7.departmentId, e7.salary) NOT IN (
      SELECT CONCAT(e8.departmentId, MAX(e8.salary))
      FROM (
        SELECT e9.salary, e9.departmentId
        FROM Employee e9
        WHERE CONCAT(e9.departmentId, e9.salary) NOT IN (
          SELECT CONCAT(e10.departmentId, MAX(e10.salary))
          FROM Employee e10
          GROUP BY e10.departmentId
        )
      ) e8
      GROUP BY departmentId
    ) and CONCAT(departmentId, salary) NOT IN (
      SELECT CONCAT(employee.departmentId, MAX(employee.salary))
      FROM Employee employee
      GROUP BY departmentId
    )
  ) e6
  GROUP BY e6.departmentId
)
