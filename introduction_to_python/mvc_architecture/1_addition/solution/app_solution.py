from model_solution import store
from view_solution import capture_number_1,capture_number_2,display
number_1= capture_number_1()
number_2= capture_number_2()

result= number_1 + number_2
display(result)
store(number_1,number_2,result)
