class Person:
    def __init__(self,name,age,spouse=[],children=[]):
        self.name=name
        self.age=age
        self.spouse=spouse
        self.children=children
    def get_divorced(self):
        if self.spouse != None:
            spouse1=self.spouse
            # print(spouse1)
            self.spouse=None
            spouse1.spouse=None

class Child(Person):
    def __init__(self,name,age,spouse,children,parents):
        super().__init__(name,age,spouse,children)
        self.parents=parents

John = Person("John", 31)
Kathy = Person("Kathy", 29, John, [])
John.spouse=Kathy
# print(John.spouse.name)
print(John.get_divorced()) # == None
print(John.spouse) #== None
print(Kathy.spouse)# == None