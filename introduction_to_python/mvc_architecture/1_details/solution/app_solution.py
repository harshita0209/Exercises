from view_solution import capture_age,capture_name,display
from model_solution import store
name=capture_name()
age=capture_age()

info=display(name,age)
print(store(name,age))