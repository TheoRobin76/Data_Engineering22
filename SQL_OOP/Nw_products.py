import pyodbc


class NwProducts:

    def __init__(self):
        self.server = 'localhost,1433'
        self.database = 'Northwind'
        self.username = 'SA'
        self.password = 'Passw0rd2018'
        self.docker_Northwind = pyodbc.connect('DRIVER={SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.docker_Northwind.cursor()

    def _sql_query(self, sql_query):
        return self.cursor.execute(sql_query)

    def print_all_product_records(self):
        query_records = self._sql_query("SELECT * FROM Products")
        while True:
            record = query_records.fetchone()
            if record is None:
                break
            print(record)

    def print_average_unit_price(self):
        query_records = self._sql_query("SELECT * FROM Products")
        # total = 0 #Matt's Method
        # number = 0
        # while True:
        #     record = query_records.fetchone()
        #     if record is None:
        #         break
        #     total += record.UnitPrice
        #     number += 1
        # print(total/number)

        total_unit_price = [] #Danny's Method
        while True:
            record = query_records.fetchone()
            if record is None:
                break
            total_unit_price.append(record.UnitPrice)

        print(sum(total_unit_price)/len(total_unit_price))




