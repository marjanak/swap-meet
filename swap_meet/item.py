import uuid

class Item:
    def __init__(self, id=None):
        self.id = uuid.uuid4().int if id == None else id
    def __str__(self):
        return f"An object of type Item with id {self.id}"
    
       
    def get_category(self):
        return "Item"
        