my_inventory = ["Sword", "Shield", "Bow", "Potions"]

print(f"Current inventory: {my_inventory}")

new_item = "Crystal Sceptre"

my_inventory.append(new_item)

print(f"Inventory after pickup: {my_inventory}")

my_inventory.pop()

print(f"Inventory after dropping last item: {my_inventory}")