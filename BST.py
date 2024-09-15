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


    def search(self, val): # check existance of val in the tree
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

    
    def find_min(self):
        while self.left:
            self = self.left
        return self.data

    
    def find_max(self):
        while self.right:
            self = self.right
        return self.data


    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None and self.right:
                return self.right
            if self.right is None and self.left:
                return self.left
            #both
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)
                
        return self


    def _get_node(self, val): # return the node with val
        if self.data == val:
            return self
        
        if val < self.data:
            if self.left:
                return self.left._get_node(val)
            else:
                return None
        
        if val > self.data:
            if self.right:
                return self.right._get_node(val)
            else:
                return None

