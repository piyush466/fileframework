class Employee:
    name = "piyush"
    salary = 1000
    bonous = 4500


    @property
    def totoalsalary(self):
        return self.salary + self.bonous


    @totoalsalary.setter
    def totoalsalary(self, val):
        self.bonous = val - self.salary
            # 4500=    -1000
e = Employee()
print(e.totoalsalary)
e.totoalsalary = 5800
print(e.salary)
print(e.bonous)
