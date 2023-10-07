SELECT (FirstName + '.' + LastName + '@softuni.bg') AS [Full Email Address]
FROM Employees

SELECT FirstName + ' ' + MiddleName + ' ' + LastName AS [Full Name] 
FROM Employees
WHERE Salary IN (25000, 14000, 12500 , 23600)


CREATE VIEW [V_EmployeesSalaries] AS 
SELECT FirstName, LastName, Salary 
FROM Employees



CREATE VIEW V_EmployeeNameJobTitle
AS
(SELECT 
	CONCAT(FirstName,' ', ISNULL(MiddleName,''),' ',LastName) AS [Full Name],
	JobTitle
FROM Employees)


SELECT * FROM V_EmployeeNameJobTitle


SELECT TOP(7) FirstName, LastName, HireDate  FROM Employees
ORDER BY HireDate DESC

SELECT * FROM Departments

UPDATE Employees
SET Salary *= 1.12
WHERE DepartmentID IN (1,2,4,11)

SELECT Salary FROM Employees


GO