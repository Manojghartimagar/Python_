# Write a class Train which has methods to book a ticket , get status {no of seats} and get fare inforamation of trains running under Indian Railways. 

class Train:

    def __init__(self, name, seats, fare):
        self.name = name
        self.seats = seats
        self.fare = fare

    def getStatus(self):
        print("------ Train Status ------")
        print(f"Train Name : {self.name}")
        print(f"Available Seats : {self.seats}")

    def getFareInfo(self):
        print("------ Fare Information ------")
        print(f"Ticket Price : Rs {self.fare}")

    def bookTicket(self):
        if self.seats > 0:
            print(f"Ticket booked successfully in {self.name}")
            print(f"Your seat number is {self.seats}")
            self.seats -= 1
        else:
            print("Sorry! No seats available")