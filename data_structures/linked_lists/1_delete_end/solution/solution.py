class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def _delete_at_end(self):
        if self.next.next == None:
            self.next = None
        else:
            return self.next._delete_at_end()


class linkedlist:
    def __init__(self, head=None):
        self.head = head

    def delete_at_end(self):
        if self.head==None:
            return None
        elif self.head.next==None:
            self.head==None
            return self
        else:
            return self.head._delete_at_end()
items = linkedlist()
items.head = Node(20)
items.head.next = Node(30)
items.head.next.next = Node(50)
# print(items.head.data, items.head.next.data, items.head.next.next.data)
print(items.delete_at_end())
# print(items.head.data)