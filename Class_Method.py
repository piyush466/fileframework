class clasmethod:
    emp = "piyush"
    salary = 1000
    postion = "testing"


    @classmethod
    def good(cls, sal):
        cls.salary = sal

c = clasmethod()
print(c.salary)
c.good(700)
print(c.salary)

print(clasmethod.salary)


