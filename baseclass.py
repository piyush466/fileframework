class building:
    company = "Cliffex"

    def newC(self):
        print("i m base class")


class building2(building):
    # company = "google"

    def bag(self):
        print("test ")


b = building()
b1 = building2()
b.newC()
print("********", b.company, "*******")

print(b1.company)
b1.bag()