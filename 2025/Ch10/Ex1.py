'''
. Create a class “Programmer” for storing information of few programmers
working at Microsoft.
'''

class Programmer:
    company = "Microsoft"
    def __init__(self, name, language, salary):
        self.name = name
        self.language = language
        self.salary = salary

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod
    def greet(name):
        print(f"Good Morning {name}")

    def __str__(self):
        return f"Name: {self.name} Language: {self.language} Salary: {self.salary}"

manju = Programmer("Manju", "C++", 2000000)
manju.getInfo()
manju.greet(manju.name)
print(manju.company)
