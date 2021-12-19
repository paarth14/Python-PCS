# Write a Class Train which has methods to book a ticket, get status (no. of seats), cancel a ticket and get fare information of the train running under the Indian Railways.

class Train:
    def __init__(self, name, fare, seat):
        self.name = name
        self.fare = fare
        self.seat = seat
    
    def getStatus(self):
        print("************")
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are: {len(self.seat)}")
        
    def fareInfo(self):
        print(f"The fare of the train is: {self.fare}")
        print("************")
    
    def bookTicket(self):
        if len(self.seat) > 0:
            print(f"Congratulations, Your ticket has been successfully booked and Your seat number is {len(self.seat)}")
            self.seat.pop()
        else:
            print(f"Sorry, You need to try in Tatkal")
    
    def cancelTicket(self, num):
        self.seat.append(num)
        print(f"CONFIRMATION ! YOUR SEATS ARE CANCELLED \nSEAT NO. CANCELLED {num}")
        
information = Train("Deccan Express: 41015", 90, [1,2,3,4,5,6,7,8,9,10])
information.getStatus()
information.fareInfo()
information.bookTicket()
information.bookTicket()
information.getStatus()
information.cancelTicket(10)
information.getStatus()
