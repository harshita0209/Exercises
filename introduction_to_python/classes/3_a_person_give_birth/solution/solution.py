class Person:
    def __init__(self,name, age,spouse=None,children=[]):
        self.name = str(name)
        self.age = age
        self.spouse = spouse
        self.children = children
    def give_birth(self,name):
        child=Child(name,0,parents=[self])
        self.children.append(child)
        if self.spouse:
            self.spouse.children.append(child)
            child.parents.append(self.spouse)

class Child(Person):
    def __init__(self, name, age, spouse=None,children=[], parents=[]):
        super().__init__(name, age,spouse,children)
        self.parents = parents
Jonny = Person("Jonny", 32, None, [])
Beth = Person("Beth", 28, Jonny, [])
Jonny.spouse = Beth
Beth.give_birth("Sam")
print(Beth.children)