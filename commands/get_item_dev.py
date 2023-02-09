def get_item_dev(inventory, all_ressources, recipes):
    inp = input("What do you want to add?: (tools/pickaxe/1)(items/stone/4):").split("/")
    print(inventory)
    print(inventory[inp[0]])
    print(float(inp[2]))
    inventory[inp[0]][inp[1]] = float(inp[2])
    return inventory
