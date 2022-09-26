import logging

class Node:
    def __init__(self,data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None


    def printing(self):
        if self.head is None:
            print("The list in empty") 
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def insert_at_begining(self, data):
        print("Inserting at the head = ", data)
        node = Node(data, self.head)
        self.head = node
        
    def length_of_ll(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        print("The lenght of LinkedList  is ", count)
        
    def insert_at_end(self, data):
        print("Inserting at the end = ", data)
        node = Node(data, None)
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node
        
    def insert_at(self, index, data):
        print("Inserting at inde x = ", index)
        itr = self.head
        num = 0
        while itr:
            if num == index - 1:
                node = Node(data, itr.next)
                itr.next = node  
            itr = itr.next
            num += 1         
                    
if __name__ == "__main__":
    print("***Wellcome to Linked List****")
    ll = LinkedList()
    ll.length_of_ll()
    ll.insert_at_begining(10)
    ll.length_of_ll()
    ll.printing()
    ll.insert_at_begining(12)
    ll.printing()
    ll.length_of_ll()
    ll.insert_at_end(121)
    ll.printing()
    ll.insert_at_begining([12,13,14,15])
    ll.printing()
    ll.insert_at(1,25)
    ll.length_of_ll()
    ll.printing()
