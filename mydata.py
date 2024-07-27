import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Adithyas",
  password="Adithya@123"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")