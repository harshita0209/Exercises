class Employee:
    def __init__(self,name,id,salary,years):
        self.name=name 
        self.id=id
        self.salary=salary
        self.years=years
        
def sort_employees(employee_lst):
        list1=[]
        for i in employee_lst:
            list1.append(i.name)
        list1.sort()
        # print(list1)
        return list1
    
