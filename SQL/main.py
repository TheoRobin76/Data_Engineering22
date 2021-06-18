import pyodbc

server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
docker_Northwind = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = docker_Northwind.cursor()


cursor.execute("SELECT @@version;")
row = cursor.fetchone()
# print(row)

# cust_rows = cursor.execute("SELECT * FROM Customers;").fetchall()
# print(cust_rows)

# rows = cursor.execute("SELECT * FROM Products;").fetchall() #this method can swamp the memory
#
# for record in rows:
#     print(record.UnitPrice)

rows = cursor.execute("SELECT * FROM Products;") #this method is better than the fetchall() method

while True:
    record = rows.fetchone()
    if record is None:
        break
    print(record.UnitPrice)

