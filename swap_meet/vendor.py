from swap_meet.item import Item

class Vendor:
    def __init__(self,inventory=None):
        self.inventory= inventory
        self.inventory= [] if self.inventory is None else self.inventory
        
    def add(self,item):
        
        self.inventory.append(item)
        return item
    
    def remove(self,item):
    
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
        return item
    
    def get_by_id (self,item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
            else:
                return None
            
    def swap_items(self,other_vendor, my_item, their_item):
        for item in self.inventory:
            if item not in self.inventory:
                return False
            elif their_item not in other_vendor.inventory:
                return False
            else:
                other_vendor.inventory.append(my_item)
                self.inventory.append(their_item)
                self.inventory.remove(my_item)
                other_vendor.inventory.remove(their_item)
            return True
        
    def swap_first_item(self, other_vendor):
        if len(self.inventory) > 0 and len(other_vendor.inventory) > 0:
            first_item = self.inventory[0]
            other_first_item = other_vendor.inventory[0]

            self.inventory.remove(first_item)
            other_vendor.inventory.append(first_item)
            other_vendor.inventory.remove(other_first_item)
            self.inventory.append(other_first_item)

            return True
        else:
            return False
        



    

