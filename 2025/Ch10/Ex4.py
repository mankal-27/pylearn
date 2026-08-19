'''
Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
and get fare information of train running under Indian Railways
'''

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The train {self.name} has {self.seats} seats. The fare is {self.fare}")

    def bookTicket(self):
        if (self.seats > 0):
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry! All seats are booked")

    def cancelTicket(self):
        print(f"Your ticket has been cancelled! Your seat number is {self.seats}")
        self.seats = self.seats + 1

    def getFareInfo(self):
        print(f"The price of a ticket is {self.fare}")

    def getSeatsInfo(self):
        print(f"The number of seats available are {self.seats}")

    def __str__(self):
        return f"Name: {self.name} Fare: {self.fare} Seats: {self.seats}"

t = Train("Chennai Express", 100, 5)
print(t)
t.getStatus()
t.bookTicket()
t.getStatus()
t.cancelTicket()
t.getStatus()
t.getFareInfo()
t.getSeatsInfo()