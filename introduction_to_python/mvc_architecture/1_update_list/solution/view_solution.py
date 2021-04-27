from model_solution import get_store,update_fruit
def show_fruits(data):
    get_store(data)

def ask_fruit():
    fruit=input("Enter fruit to add")
    data=update_fruit(fruit)
    show(data)
def show(data):
    show_fruits(data)

