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

    def insert_at(self, data, place):
        if place == 0:
            return self.push_front(data)
        elif place<0 or place>self.len() + 1:
            raise Exception("Invalide place, index out of range")
        elif place == slef.len() + 1:
            return self.push_back(data)
        else:
            index = 1
            itr = self.head
            while itr:
                if index == place:
                    itr.next = Node(data, itr.next)
                    return
                itr = itr.next
                index += 1
                


