import abc

#from game import GameState
from inventory import Inventory

player1 = Inventory("Player")
test = player1.getInventory()
print(f"This is the contents of the Player inventory: {test}")

print("--------------------------------------------------")

player2 = Inventory("Dealer")
test2 = player2.getInventory()
print(f"This is the contents of the Dealer inventory: {test2}")

player1.useItem("beer")
print(f"This is now the current contents for the Player: {test}")