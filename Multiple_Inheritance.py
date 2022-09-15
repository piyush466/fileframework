#multiple inheritance 
class parent1:
    company = "Visa"

    def good(self):
        print("i m parent 1")


class parent2:
    company = "google"

    def test(self):
        print("i m parent 2")



class child(parent1,parent2):

     def piyush(self):
         print("testing")

c = child()
c.piyush()
print(c.company)
c.good()
c.test()
