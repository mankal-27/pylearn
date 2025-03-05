'''
. Can you change the self-parameter inside a class to something else (say
“harry”). Try changing self to “slf” or “harry” and see the effects.
'''

class Employee:
    def __init__(slf, name, language, salary):
        slf.name = name
        slf.language = language
        slf.salary = salary

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod
    def greet(name):
        print(f"Good Morning {name}")

    def __str__(self):
        return f"Name: {self.name} Language: {self.language} Salary: {self.salary}"

manju = Employee("Manju", "C++", 2000000)
manju.getInfo()
manju.greet(manju.name)
print(manju)