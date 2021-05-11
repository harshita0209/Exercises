class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self, head=None):
        self.head = head
    def insert_at_start(self,data):
        if self.head==None:
            return None
        else:
            n=Node(data)
            # print(n)
            n.next=self.head
            self.head=n
items = linkedList()
items.head = Node(20)
items.insert_at_start(40)
items.insert_at_start(50)
print(items.head.data)# == 50
print(items.head.next.data) #== 40
print(items.head.next.next.data)# == 20