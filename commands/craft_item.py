import time


def craft_item(inventory, recipes, needed_time_per_item):
    item_to_craft, count = input("What do you want to craft?: (steel*1)").split("*")
    all_craftable_things = {}
    ressources_for_crafting = {}
    # get all craftable items in a dictonary -> key = repair tool -- value = tool
    for item in recipes.keys():
        all_craftable_things[item.split("|")[0]] = item.split("|")[1]
    # get recipe for user's item
    recipe = recipes.get(item_to_craft + "|" + all_craftable_things.get(item_to_craft))
    # save all ressources for crafting in a list
    if item_to_craft in all_craftable_things.keys():
        for item in recipe:
            ressources_for_crafting[item.split("*")[0]] = float(item.split("*")[1]) * int(count)
        print(ressources_for_crafting)
        # check if user has all items he needs
        new_inv = delete_items_from_inventory(inventory=inventory["items"], inventory_to_delete=ressources_for_crafting)
        if not new_inv[0]:
            # returns exeption to user
            return new_inv[1], False
        else:
            # wait until crafting time is over
            print(f"crafting... Needed time: {needed_time_per_item * float(count)}")
            time.sleep(needed_time_per_item * float(count))
            # delete ressources from inventory
            inventory["items"] = new_inv[1]
            # append new item to inventory
            if all_craftable_things.get(item_to_craft) == "tools":
                # count becomes durability
                count = 100
            # check if user already has the crafted item in the inventory
            if item_to_craft in inventory[all_craftable_things.get(item_to_craft)]:
                inventory[all_craftable_things.get(item_to_craft)][item_to_craft] += float(count)
            else:
                inventory[all_craftable_things.get(item_to_craft)][item_to_craft] = float(count)
            return inventory, True
    else:
        return "The item doesn't exists!", False


def delete_items_from_inventory(inventory, inventory_to_delete):
    # loops through each item for the ressources in the recipe
    for item, count in inventory_to_delete.items():
        # checks if user has the item
        if item in inventory.keys():
            # checks if user has the count of the items
            if float(inventory.get(item)) >= float(count):
                if float(inventory.get(item)) == float(count):
                    # delete item from inv
                    inventory.pop(item)
                else:
                    inventory[item] -= count
            else:
                return False, f"You don't have {count} of {item}. You only have {inventory.get(item)}"
        else:
            return False, f"You don't have the item {item} in you're inventory, which you need"

    return True, inventory


### EXAMPLE USAGE ####
example = False
if example:
    recipes = {
        "steel|items": ["iron*1", "match*1"],
        "match|items": ["stick*1", "coal*0.25"],
        "stick|items": ["wood*1"],
        "engine|items": ["steel*10", "copper wire*5", "fuel tank*1", "spark plug*1"],
        "spark plug|items": ["cooper*5", "nickel*2", "insulator*1"],
        "insulator|items": ["rubber*5", "glass*2"],
        "glass|items": ["sand*1", "match*1"],
        "cooper wire|items": ["cooper*2"],
        "fuel tank|items": ["rubber*2", "steel*5"],
        "repair kit|tools": ["insulator*1", "nickel*1"]
    }
    inventory = {"tools": {"pickaxe": 100.0, "wrench": 100, "shovel": 92.5, "axe": 95.0},
                 "items": {"stone": 4.0, "stick": 2.0, "rubber": 10, "iron": 9.0, "match": 3, "sand": 15, "coal": 50,
                           "insulator": 1, "nickel": 23, "steel": 2}}
    needed_time = 0.25
    craft_itemm = craft_item(inventory, recipes, needed_time)
    if craft_itemm[1]:
        inventory = craft_itemm[0]
    else:
        print(craft_itemm[0])
    print(inventory)
