class Categories:
    all = {}#this is a dict that will hold all the categories by there (id)

    def __init__(self, name, id= None): #this is the initialization
        self.id = id
        self.name = name

    @classmethod
    def add_category(cls, name):
        pass

    def __repr__(self):
        return f"<Categories {self.id}: {self.name}>" #making sure that when we print a category it will look like this as strings

    

      