import random

class Inventory:
    def __init__(self, character):
        self.character = character
        self.selectedItemsOptions = ["beer", "cigarette", "handsaw", "magnifiers"]
        self.InventorySpace = 6
        self.characterInventory = []

    def getInventory(self):
        for i in range(random.randint(2, self.InventorySpace)):
            self.characterInventory.append(random.choice(self.selectedItemsOptions))
        return(self.characterInventory)
    
    def useItem(self, inventory):
        try:
            self.characterInventory.remove(inventory)
            return print(f"The item {inventory} was removed.")
        except:
            return print("This item does not exist")