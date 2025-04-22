class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getName(self):
        print(self.name)
    def getAge(self):
        print(self.age)

class Employee(Person):
    def __init__(self, name, age, employeeid):
        super().__init__(name, age)
        self.employeeid = employeeid

    def getID(self):
        print(self.name, self.age, self.employeeid)

myId = Employee("IoT", 65, 2018)
myId.getID()