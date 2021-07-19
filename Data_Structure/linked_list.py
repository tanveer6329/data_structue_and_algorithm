# A single node of a singly linked list
class Node:
    # constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# A Linked List class with a single head node       
class LinkedList:
    def __init__(self):
        # this is executed only once, when LinkedList is called
        # when first element is entered head points to nothhing/none
        self.head = None 

    # Insertion
    # inserting element at the beginning of the linked list
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    

    # Insertion
    # inserting element at the end of the linked list
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)


    # converting a python list into a linked_list
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    
    # returning the length of a linked_list
    def get_length(self):
        count=0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count

    # removing an item from linked list at a particular index
    def remove_at(self, index):
        if index<0 and index>= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1

    # inserting a value to a linked_list at a particular index
    def insert_at(self, index, data):
        if index<0 and index>self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count+=1
        
    # printing the linked list 
    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)



if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(['banana', 'mango', 'orange', 'grapes'])
    print(ll.get_length())
    #ll.remove_at(3)
    ll.insert_at(2, 'guava')
    ll.print()





