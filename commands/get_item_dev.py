def get_item_dev(inventory):
    compartant, item, count = input("What do you want to add?: (tools/pickaxe/1)(items/stone/4):").split("/")
    inventory[compartant][item] = float(count)
    return inventory, True
