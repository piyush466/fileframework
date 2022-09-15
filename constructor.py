class python:

    def __init__(self,name,surname,address):
        self.name = name
        self.surname = surname
        self.address =address


    def details(self):
        print(f"name is {self.name}")
        print(f"surname is {self.surname}")
        print(f"address is {self.address}")


obj = python("piyush", "Dravyakar", "d46 noida")
obj.details()