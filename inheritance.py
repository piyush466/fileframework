#single level inheritance
class A:
    def cA(self):
        print("A class")

class B:
    def cB(self):
        print("B class")

class C(A,B):
    def cC(self):
        print("C class")


o = C()
o.cA()
o.cB()
o.cC()