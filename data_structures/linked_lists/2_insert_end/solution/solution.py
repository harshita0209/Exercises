class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def _insert_at_end(self,data):
        if self.next==None:
            self.next=Node(data)
        else:
            return self.next._insert_at_end(data)


class linkedList:
    def __init__(self, head=None):
        self.head = head
    def insert_at_end(self,data):
        if self.head==None:
            return None
        elif self.head.next==None:
            self.head=Node(data)
        else:
            return self.head._insert_at_end(data)

items = linkedList()
items.head = Node(20)
items.head.next = Node(30)
items.insert_at_end(40)

print( items.head.data)# == 20
print( items.head.next.data )#== 30
print( items.head.next.next.data)# == 40