class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    def _search(self,x):
        if self.data==x:
            return True
        elif self.next==None:
            return False
        else:
            return self.next._search(x)

class linkedList:
    def __init__(self, head=None):
        self.head = head
    def search(self,x):
        if self.head==None:
            return None
        elif self.head.data==x:
            return True
        else:
            return self.head._search(x)

items = linkedList()
items.head = Node(20)
items.head.next = Node(30)
items.head.next.next = Node(40)

print(items.search(30))# == True
print(items.search(10))# == False