class company:

    def __init__(self,name,product):
        self.name= name
        self.product = product

    def programmer(self):
        print(f"The name of programmer is {self.name} and his product name is {self.product}")


object = company("google","gmail")
piyush = company("Cliffex", "INDIEFOLIO")
object.programmer()
piyush.programmer()
