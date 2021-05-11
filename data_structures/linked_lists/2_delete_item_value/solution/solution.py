
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def _delete_item_by_value(self,x):
        if self.next.data == x and self.next.next != None:
            pre=self
            print('pre value if-',pre.data)
            pre.next=self.next.next
            self.head=self.next.next
        elif self.next.data == x and self.next.next == None:
            pre=self
            pre.next=None                  
        else:
            return self.next._delete_item_by_value(x)
        


class linkedList:
    def __init__(self, head=None):
        self.head = head

    def delete_item_by_value(self,x):
        if self.head==None:
            return None
        elif self.head.data==x:
            print('value found at first node-',self.head.data)
            self.head=self.head.next
            
            return self.head

        else:
            # print('linkedlist else')
            return self.head._delete_item_by_value(x)

items = linkedList()
items.head = Node(20)
items.head.next = Node(30)
items.head.next.next = Node(40)
items.head.next.next.next = Node(50)
items.delete_item_by_value(50)

print(items.head.data)# == 20
print(items.head.next.data)# == 30
print(items.head.next.next.data)# == 50