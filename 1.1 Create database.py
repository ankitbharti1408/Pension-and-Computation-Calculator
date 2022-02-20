import mysql.connector

pension = mysql.connector.connect(host="localhost",
 user="root", 
 password="Ab#14081999"

 )
new= pension.cursor()
new.execute("CREATE DATABASE EmployeePensionCalculatorDatabase")