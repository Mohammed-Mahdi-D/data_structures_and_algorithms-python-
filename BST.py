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

        return None


    def in_order_traversal(self):

        return None

    def pre_order_traversal(self):

        return None
    
    def post_order_traversal(self):

        return None
    
    def search(self, val):

        return None

    def delete(self, val):

        return None
