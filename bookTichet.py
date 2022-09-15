class Train:

    def __init__(self,trainName,TrainNo,Fare,Seats,):
        self.trainName = trainName
        self.Fare = Fare
        self.Seats = Seats
        self.TrainNo = TrainNo


    def status(self):
        print("********************************")
        print(f"Your tarin number is {self.TrainNo} and train mane is {self.trainName} and total fare of journey is {self.Fare} Now avaliable seats is {self.Seats - 1} ")

    def BookTicket(self):
        if(self.Seats>0):
            print("********************************")
            print(f"your ticket is book and number is {self.Seats}")
            self.Seats = self.Seats - 1

        else:
            print("try in tatkal ")




object = Train("Intercity",12604,90,20)
object.status()
object.BookTicket()
object.BookTicket()
# object.cancelTicket()
# object.status()
# object.BookTicket()
# object.BookTicket()
# object.BookTicket()