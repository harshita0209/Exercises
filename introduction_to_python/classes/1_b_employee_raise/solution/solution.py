class Employee:
    def __init__(self,name,id,salary,years):
        self.name=name 
        self.id=id
        self.salary=salary
        self.years=years
        

def give_raises(employee_lst):
    for emp in employee_lst:

        if emp.years <=5:
            emp.salary=emp.salary + 5000
        elif emp.years > 5 and emp.years < 10:
            emp.salary=emp.salary + 8000
        elif emp.years >= 10:
            emp.salary=emp.salary + 10000    
emp1 = Employee("John", 1, 45000, 8)
emp2 = Employee("Jane", 2, 22000, 1)
emp3 = Employee("Marie", 3, 90000, 10)

give_raises([emp1, emp2, emp3])
print(emp3.salary)

            