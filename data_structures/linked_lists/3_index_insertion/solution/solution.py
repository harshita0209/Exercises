class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
   
class linkedList:
    def __init__(self, head=None):
        self.head = head
    def insert_at_index(self,index,data):
        count=1
        if self.head==None:
            return None
        elif index==1:
            n=Node(data)
            n.next=self.head
            self.head=n
        else:      
            
            while self.head.next !=None :
                pre=self.head
                count += 1
                # print('count-',count,pre.data)
                if index==count:
                    # print(pre.data)
                    n=Node(data)
                    
                    # print(pre.data)
                    n.next=self.head.next
                    pre.next=n
                    break
                    # print(index)
                    # print(n.data)
                    
                self.head=self.head.next

                
items = linkedList()
items.head = Node(20)
items.head.next = Node(30)
items.head.next.next = Node(40)
items.insert_at_index(3, 2)

print(items.head.data)# == 20
print(items.head.next.data)# == 2
print(items.head.next.next.data)
# print(items.head.next)