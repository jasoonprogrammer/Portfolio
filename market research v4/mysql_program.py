import mysql.connector
from mysql.connector.errors import ProgrammingError, DatabaseError

db = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "root",
	database = "testdatabase"
	)

c = db.cursor()
try:
	c.execute("CREATE DATABASE testdatabase")
except DatabaseError as e:
	print(e)
	
try:
	c.execute(
		"""CREATE TABLE Person2
		(
		name VARCHAR(50),
		age smallint UNSIGNED,
		personID int PRIMARY KEY AUTO_INCREMENT
		)"""
		)
except ProgrammingError as e:
	print(e)

for x in c:
	print(x)
	print("person" in x)