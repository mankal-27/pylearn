class Employee:
    company = "Google"
    def show(self):
        print(f"The name is {self.company} and the salary is {self.salary}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"The language is {self.language}")

class Programmer(Employee,Coder):
    company = "Microsoft"
    def showLanguage(self):
        print(f"The name is {self.company} and the language he/she is good at {self.language}")

a = Employee()
b = Programmer()

b.showLanguage()
b.printLanguage()