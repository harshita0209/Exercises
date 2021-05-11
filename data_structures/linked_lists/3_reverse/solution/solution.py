class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self, head=None):
        self.head = head
    
    def reverse(self):
        previous = None
        current = self.head
        while current:                        
            next = current.next             
            current.next = previous         
            previous = current              
            current = next 
        self.head = previous 
        return self
items = linkedList()
items.head = Node(20)
items.head.next = Node(30)
items.head.next.next = Node(40)
items.reverse()

print(items.head.data) #== 40
print(items.head.next.data)# == 30
print(items.head.next.next.data)
