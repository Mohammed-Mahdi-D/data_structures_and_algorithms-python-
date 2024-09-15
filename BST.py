class BST():
    def __inti__(self, data):
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

        return None


    def in_order_traversal(self):

        return None

    def pre_order_traversal(self):

        return None
    
    def post_order_traversal(self):

        return None
    
    def search(self, val): # only check the existance return true/false
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
