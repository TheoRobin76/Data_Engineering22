# class Person:
#     def __init__(self, name, age = 0):
#         self.name = name
#         self.__age = age
#
#     # def display(self):
#     #     print(self.name)
#     #     print(self.__age)
#     #
#     def getAge(self):
#         print(self.__age)
#
#     def setAge(self, age):
#         self.__age = age
#
#
# Ola = Person("Ola", 75)
# #
# # Ola.display()
# #
# # Ola.__age = 50 #dunder means the variable doesn't change, single _ alows you to change it but makes it slightly harder
# # Ola.display()
#
# Ola.setAge(26)
# Ola.getAge()
#
import datetime
class Employee:
    def __init__(self, EmployeeID, Name, Age, DOB, JobTitle, JobDescription, Salary, Status):
        self.__EmployeeID = EmployeeID
        self.__Name = Name
        self.__Age = Age
        self.__JobTitle = JobTitle
        self.__JobDescription = JobDescription
        self.__Salary = Salary
        self.__DOB = DOB
        self.__Status = Status

    def SetEmployeeID(self, EmployeeID):
        if len(EmployeeID) == 7 and isinstance(int(EmployeeID), int):
            self.__EmployeeID = EmployeeID
        else:
            return "Not valid"

    def GetEmployeeID(self):
        return self.__EmployeeID

    def SetName(self, Name):
        numbers = ["0","1","2","3","4","5","6","7","8","9"]
        valid = True
        for number in numbers:
            if number not in Name:
                valid = True
            else:
                valid = False
                break
        if valid == True:
            self.__Name = Name
        else:
            return "Not Valid"

    def GetName(self):
        return self.__Name

    def SetAge(self, Age):
        if Age > 18 and Age <80 and isinstance(Age, int):
            self.__Age = Age

    def GetAge(self):
        return self.__Age

    def SetDOB(self, DOB):
        if isinstance(DOB, datetime.date):
            self.__DOB = DOB

    def GetDOB(self):
        return self.__DOB

    def SetJobTitle(self, JobTitle):
        self.__JobTitle = JobTitle

    def GetJobTitle(self):
        return self.__JobTitle

    def SetJobDescription(self, JobDescription):
        self.__JobDescription = JobDescription

    def GetJobDescription(self):
        return self.__JobDescription

    def SetSalary(self, Salary):
        if Salary > 10000 and Salary < 1000000000:
            self.__Salary = Salary

    def GetSalary(self):
        return self.__Salary

    def SetStatus(selfself, Status):
        if Status == "Active" or Status == "Fired" or Status == "Retired":
            self.__Status = Status

    def Bio(self):
        print(f"Employee ID: {self.__EmployeeID}")
        print(f"Name: {self.__Name}")
        print(f"Date of Birth: {self.__DOB}")
        print(f"Age: {self.__Age}")
        print(f"Job Title: {self.__JobTitle}")
        print(f"Job Description: {self.__JobDescription}")
        print(f"Salary: £{self.__Salary}")
        print(f"Status: {self.__Status}")
        return ""

    def Raise(self, percentage = 5):
        multiplier = 1 + (percentage/100)
        self.__Salary = int(self.__Salary * multiplier)

David = Employee("0000001", "David Lilley", 26, datetime.date(1995, 1, 30), "Junior Consultant", "Training", 25000, "Retired")
Theo = Employee("0000002", "Theo Gluckstein", 28, datetime.date(1993, 3, 22), "Junior Consultant", "Training", 0, "Active")

print(Theo.Bio())
