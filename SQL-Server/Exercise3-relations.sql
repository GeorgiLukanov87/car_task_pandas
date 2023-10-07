CREATE DATABASE [Exercise3-relations]

USE [Exercise3-relations]


CREATE TABLE Passports(
	PassportID INT PRIMARY KEY,
	PassportNumber char(8) NOT NULL,
)

-- 01. One-To-One Relationship

CREATE TABLE Persons(
	PersonID INT PRIMARY KEY NOT NULL,
	FirstName nvarchar(30) NOT NULL,
	Salary DECIMAL(7,2) NOT NULL,
	PassportID INT FOREIGN KEY REFERENCES Passports(PassportId) NOT NULL UNIQUE
)

INSERT INTO Passports
	VALUES
			(101, 'N34FG21B'),
			(102, 'K65LO4R7'),
			(103, 'ZE657QP2')

INSERT INTO Persons
	VALUES
			(1,'Roberto', 43300, 102),
			(2,'Tom', 56100, 103),
			(3,'Yana', 60200, 101)

SELECT FirstName,Salary,PassportNumber FROM Persons as p
	JOIN Passports as ps ON p.PassportID = ps.PassportID


-- 02. One-To-Many Relationship


CREATE TABLE Manufacturers(
	ManufacturerID INT PRIMARY KEY,
	[Name] NVARCHAR(30) NOT NULL,
	EstablishedOn DATE NOT NULL,
)

CREATE TABLE Models(
	ModelID INT PRIMARY KEY,
	[Name] NVARCHAR(30) NOT NULL,
	ManufacturerID INT FOREIGN KEY
	REFERENCES Manufacturers(ManufacturerID) NOT NULL,
)


INSERT INTO Manufacturers
	VALUES
			(1, 'BMW', '03/07/1916'),
			(2, 'Tesla', '01/01/2003'),
			(3, 'Lada', '05/01/1966')


INSERT INTO Models
	VALUES
			(101, 'X1', 1),
			(102, 'i6', 1),
			(103, 'Model S', 2),
			(104, 'Model X', 2),
			(105, 'Model 3', 2),
			(106, 'Nova', 3)


SELECT mo.ModelID,mo.[Name],ma.EstablishedOn FROM Models AS mo
	JOIN Manufacturers AS ma ON mo.ManufacturerID = mo.ManufacturerID


-- 03. Many-To-Many Relationship

CREATE TABLE Students(
	StudentID INT PRIMARY KEY,
	[Name] varchar(50) NOT NULL,
)

CREATE TABLE Exams(
	ExamID INT PRIMARY KEY,
	[Name] varchar(50) NOT NULL,
)

CREATE TABLE StudentsExams(
	StudentID INT FOREIGN KEY REFERENCES Students(StudentID),
	ExamID INT FOREIGN KEY REFERENCES Exams(ExamID),
	-- Composite key
	PRIMARY KEY(StudentID,ExamID)
)

INSERT INTO Students
	VALUES
			(1, 'Mila'),
			(2, 'Toni'),
			(3, 'Ron')

INSERT INTO Exams
	VALUES
			(101, 'SpringMVC'),
			(102, 'Neo4j'),
			(103, 'RonOracle 11g')

INSERT INTO StudentsExams
	VALUES
		(1, 101),
		(1, 102),
		(2, 101),
		(3, 103),
		(2, 102),
		(2, 103)

SELECT * FROM Students AS s
	JOIN StudentsExams as se ON s.StudentID = se.StudentID
	JOIN Exams AS e ON e.ExamID = se.ExamID

-- 04. Self-Referencing

CREATE TABLE Teachers(
	TeacherID INT PRIMARY KEY,
	[Name] NVARCHAR(50) NOT NULL,
	ManagerID INT FOREIGN KEY REFERENCES Teachers(TeacherID)
)

INSERT INTO Teachers
	VALUES
			(101,'John',NULL),
			(102,'John',106),
			(103,'John',106),
			(104,'John',105),
			(105,'John',101),
			(106,'John',101)


--05. Online Store Database

USE [Exercise3-relations]

CREATE TABLE Cities(
	CityID INT PRIMARY KEY,
	[Name] VARCHAR(50) NOT NULL,
)

CREATE TABLE Customers(
	CustomerID INT PRIMARY KEY,
	[Name] VARCHAR(50) NOT NULL,
	Birthday DATE,
	CityID INT FOREIGN KEY REFERENCES Cities(CityID)
)

CREATE TABLE ItemTypes(
	ItemTypeID INT PRIMARY KEY,
	[Name] VARCHAR(50) NOT NULL
)

CREATE TABLE Items(
	ItemID INT PRIMARY KEY,
	[Name] VARCHAR(50) NOT NULL,
	ItemTypeID INT FOREIGN KEY REFERENCES ItemTypes(ItemTypeID)
)

CREATE TABLE Orders(
	OrderID INT PRIMARY KEY,
	CustomerID INT FOREIGN KEY REFERENCES Customers(CustomerID)
)

CREATE TABLE OrderItems(
	OrderID INT FOREIGN KEY REFERENCES Orders(OrderID),
	ItemID INT FOREIGN KEY REFERENCES Items(ItemID),
	PRIMARY KEY (OrderID, ItemID)
)

--06. University Database

CREATE TABLE Subjects(
	SubjectID INT PRIMARY KEY,
	SubjectName VARCHAR(50) NOT NULL
)

CREATE TABLE Majors(
	MajorID INT PRIMARY KEY,
	[Name] VARCHAR(50) NOT NULL
)

CREATE TABLE Students2(
	StudentID INT PRIMARY KEY,
	StudentNumber VARCHAR(5) NOT NULL,
	StudentName VARCHAR(50) NOT NULL,
	MajorID INT FOREIGN KEY REFERENCES Majors(MajorID)
)

CREATE TABLE Payments(
	PaymentID INT PRIMARY KEY,
	PaymentDate DATETIME2 NOT NULL,
	PaymentAmount DECIMAL(7,2),
	StudentID INT FOREIGN KEY REFERENCES Students2(StudentID)
)

CREATE TABLE Agenda(
	StudentID INT FOREIGN KEY REFERENCES Students2(StudentID),
	SubjectID INT FOREIGN KEY REFERENCES Subjects(SubjectID),
	PRIMARY KEY (StudentID, SubjectID)
)

--09. *Peaks in Rila
USE Geography

SELECT m.MountainRange, p.PeakName, p.Elevation FROM Mountains AS m 
	JOIN Peaks AS p ON m.Id = p.MountainId
	WHERE m.MountainRange = 'Rila'
	ORDER BY Elevation DESC


