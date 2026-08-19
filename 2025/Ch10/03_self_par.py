class Employee:
    language = "Python"
    salary = 1000000

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod
    def greet(name):
        print(f"Good Morning {name}")

manju = Employee()
manju.name = "Manju"
manju.language = "C++"
print(manju.name, manju.language, manju.salary)
manju.getInfo()
manju.greet(manju.name)