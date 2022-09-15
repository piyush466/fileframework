class ajoba:
    company2 = "teachers"

    def tech(self):
        print("i m ajoba")


class baba(ajoba):
    company = "excise department"

    def raid(self):
        super().tech()
        print("i m baba")

class piyush(baba):
    company1 = "cliffex"


    def testing(self):
        super().tech()
        print("i m tester")

a = ajoba()
b = baba()
p = piyush()
# print(p.company2)
b.raid()
# p.raid()
# p.tech()
p.testing()
# print(p.company)


