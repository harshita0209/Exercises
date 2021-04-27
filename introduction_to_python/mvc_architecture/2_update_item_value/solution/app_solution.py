from model_solution import Program
from view_solution import update_key,enter_value,display,show_list
program_list={1:"Java",2:"C++",3:"Python",4:".Net"}
obj1=Program(program_list)
result=obj1.get_list(program_list)
# show=program_list.get_list()
show_list(program_list)
key=update_key()
value=enter_value()
new_list=obj1.update_list_key(key,value,program_list)
display(new_list)
