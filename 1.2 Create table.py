import mysql.connector

pension = mysql.connector.connect(host="localhost",
 user="root",
 password="Ab#14081999",
 database="EmployeePensionCalculatorDatabase"
 )
new= pension.cursor()
data = "CREATE TABLE logintable (empid VARCHAR(205), password VARCHAR(205), mobile VARCHAR(205)  )"

new.execute(data)