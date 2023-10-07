CREATE DATABASE Minions


USE Minions


CREATE TABLE Minions(
	Id INT PRIMARY KEY  Not Null,
	Name VARCHAR(50) Not Null,
	Age INT Not Null,
)



SELECT * FROM Minions


CREAte TABLE Towns(
	Id INT PRIMARY  KEY   Not null ,
	Name VARCHAR(50) Not Null,
)


ALTER TABLE Minions
	ADD TownId INT FOREIGN KEY REFERENCES Towns(Id)


INSERT INTO Towns(Id,[Name])
	VALUES
		(1,'Sofia'),
		(2, 'Plovdiv'),
		(3, 'Varna')




INSERT INTO Minions(id,[name],age, TownId)
	VALUES
		(1, 'Kevin', 22, 1),
		(2, 'Bob', 15, 3),		
		(3, 'Steward', 15, 2)

SELECT * FROM Towns			
SELECT * FROM Minions	


TRUNCATE TABLE Minions


CREATE TABLE Users(
	Id BIGINT PRIMARY KEY IDENTITY Not Null,
	Username VARCHAR(30) UNIQUE Not Null,
	[Password] VARCHAR(26) Not Null, 
	ProfilePicture VARBINARY(MAX) CHECK(DATALENGTH(ProfilePicture) <= 900 * 1024),
	LastLoginTime DATETIME2 Not Null,
	isDeleted BIT Not Null,
)

INSERT INTO Users(Username,[Password],LastLoginTime,isDeleted)
	VALUES
	('Pesho0', '12345','12.10.2020', 0),
	('Pesho1', '12345','12.10.2020', 1),
	('Pesho2', '12345','12.10.2020', 0),
	('Pesho3', '12345','12.10.2020', 1),
	('Pesho4', '12345','12.10.2020', 0)


SELECT * FROM Users

ALTER TABLE Users
DROP CONSTRAINT PK__Users__3214EC073976CBD3

ALTER TABLE Users
ADD CONSTRAINT PK_Users_Id
PRIMARY KEY(Id)

ALTER TABLE Users
ADD CONSTRAINT CK_UsernameLenght
CHECK(LEN(Username) >= 5)

INSERT INTO Users(Username,[Password],LastLoginTime,isDeleted)
	VALUES
	('Pesho01', '12345','12.10.2020', 0)

SELECT * FROM Users

ALTER TABLE Users
ADD CONSTRAINT DF_Users_LastLoginTime
DEFAULT GETDATE() FOR LastLoginTime

INSERT INTO Users(Username,[Password],isDeleted)
	VALUES
	('Pesho021', '12345', 0)



CREATE TABLE Minions(
	Id INT PRIMARY KEY Not Null,
	[Name] NVARCHAR(50) Not Null,
	Age TINYINT
)

CREATE TABLE Towns(
	Id INT PRIMARY KEY Not Null,
	[Name] NVARCHAR(50) Not Null,
)

ALTER TABLE Minions
	ADD TownID INT FOREIGN KEY REFERENCES Towns(Id)

INSERT INTO Towns(Id, [Name])
VALUES
		(1, 'Sofia'),
		(2, 'Plovdiv'),
		(3, 'Varna')

INSERT INTO Minions(Id,[Name], Age, TownId)
VALUES
		(1, 'Kevin', 22, 1),
		(2, 'Bob', 15, 3),
		(3, 'Steward', NULL, 2)


CREATE TABLE People(
	Id BIGINT IDENTITY,
	Name NVARCHAR(200) Not Null,
	Picture BIT CHECK(DATALENGTH(Picture) <= 2000 * 1024),
	Height DECIMAL(3,2),
	[Weight] DECIMAL(4,2),
	Gender VARCHAR(1) Not Null,
	Birthdate DATE,
	Biography TEXT,
)


INSERT INTO People([Name],Gender)
VALUES
		('gogo0', 'm' ),
		('gogo1', 'm' ),
		('gogo2', 'm' ),
		('gogo3', 'm' ),
		('gogo4', 'm' )
