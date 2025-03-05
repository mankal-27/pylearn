class Employee:
    language = "Python"
    salary = 1000000

    def __init__(self, name, language, salary):
        self.name = name
        self.language = language
        self.salary = salary

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod
    def greet(name):
        print(f"Good Morning {name}")

manju = Employee("Manju", "C++", 2000000)
manju.getInfo()
manju.greet(manju.name)
