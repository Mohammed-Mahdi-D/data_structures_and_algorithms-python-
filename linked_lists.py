class Node: 
    def __init__(slef, data, next):
        self.data = data
        self.next = next

    def getnode(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, data):
        self.head = Node(data, self.head)
        return self.head

    def push_back(self, data):
        if(self.head == None):
            self.head = Node(data, None)
            return self.head
        else:
            itr = self.head
            while True:
                if itr.next == None:
                    itr.next = Node(data, None)
                    break
                else:
                    itr = itr.next
                    continue
            return itr.next
        
