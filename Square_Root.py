class Square_Root:

    def __init__(self,Number):
        self.Number = Number

    def square(self):
        print(f"the Square  of {self.Number}  cube is {self.Number **3}")

    def suareRoot(self):
        print(f"the Square root of {self.Number} is {self.Number **2}")

object = Square_Root(5)
object.square()
object.suareRoot()