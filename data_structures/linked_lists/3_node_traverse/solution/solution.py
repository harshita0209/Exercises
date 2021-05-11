class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self, head=None):
        self.head = head
    def traverse(self):
        
        printval = self.head
        while printval is not None:
            print (printval.data)
            printval = printval.next
items = linkedList()
items.head = Node(1)
e2 = Node(2)
items.head.next = e2
items.traverse()

# print(ret_val[0])# == 1
# print(ret_val[1])# == 2
