class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self, head=None):
        self.head = head
    def insert_after_item(self,x,data):
        start = self.head
        while start is not None:
            if start.data == x:
                # next_val=start.next
                print('if',Node(data).data,start.next,Node(data),Node(data).next)
                n=Node(data)
                n.next=start.next
                start.next=n
                print('if',Node(data).data,start.next,Node(data),Node(data).next)
                
            start=start.next
items = linkedList()
items.head = Node(20)
items.head.next = Node(30)
items.head.next.next = Node(50)
items.insert_after_item(30, 0)   
print(items.head.data) #== 20
print(items.head.next.data)# == 30
print(items.head.next.next.data)# == 0
print(items.head.next.next.next.data)