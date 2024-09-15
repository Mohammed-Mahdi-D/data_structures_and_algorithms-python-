class BST:
    def __init__(self, data):  
        self.data = data 
        self.right = None
        self.left = None


    def add_child(self, data):
        if data == self.data:
            return 
        else:
            if data < self.data:
                if self.left:
                    self.left.add_child(data)
                else:
                    self.left = BST(data)

            if data > self.data:
                if self.right:
                    self.right.add_child(data)

                else:
                    self.right = BST(data)


    def build_tree(elements):
        root = BST(elements[0])
        for element in elements[1:]:
            root.add_child(element)
        return root


    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()        

        return elements


    def pre_order_traversal(self):
        elements = [self.data]


        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()        

        return elements


    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        
        if self.right:
            elements += self.right.post_order_traversal()
        
        elements.append(self.data)
        return elements


    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def delete(self, val):
                
        return None



t = BST.build_tree([39, 3, 22, 5, 199, 4]) # type: ignore 
print(t.in_order_traversal())