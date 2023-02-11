import time


def craft_item(inventory, recipes, needed_time_per_item):
    item_to_craft, count = input("What do you want to craft?: (steel*1)").split("*")
    all_craftable_things = []
    ressources_for_crafting = []
    # get all craftable items in a list
    for item in recipes.keys():
        all_craftable_things.append(item.split("*")[0])
    # get recipe for user's item
    recipe = recipes.get(f"{item_to_craft}")
    if item_to_craft in all_craftable_things:
        for i in range(int(count)):
            for element in recipe:
                ressources_for_crafting.append(element)
        # zip the ressources. so for example ["stone*1", "stone*2"] -> ["stone*3"]
        ressources_for_crafting = zip_ressource_list(ressource_list=ressources_for_crafting)
        # check if user has all items he needs
        new_inv = delete_items_from_inventory(inventory=inventory["items"], inventory_to_delete=ressources_for_crafting)
        if not new_inv[0]:
            # returns exeption to user
            return new_inv[1], False
        else:
            # wait until crafting time is over
            print(f"crafting... Needed time: {needed_time_per_item * int(count)}")
            time.sleep(needed_time_per_item * int(count))
            # delete ressources from inventory
            inventory["items"] = new_inv[1]
            # append new item to inventory
            inventory["items"][item_to_craft] = int(count)
            return inventory, True
    else:
        return "The item doesn't exists!", False


def delete_items_from_inventory(inventory, inventory_to_delete):
    # loops through each item for the ressources in the recipe
    for item, count in inventory_to_delete:
        # checks if user has the item
        if item in inventory.keys():
            # checks if user has the count of the items
            if inventory.get(item) >= count:
                if inventory.get(item) == count:
                    # delete item from inv
                    inventory.pop(item)
                else:
                    inventory[item] -= count
            else:
                return False, f"You don't have {count} of {item}. You only have {inventory.get(item)}"
        else:
            return False, f"You don't have the item {item} in you're inventory, which you need"

    return True, inventory


def zip_ressource_list(ressource_list):
    # self-explanatory
    result = {}
    for item in ressource_list:
        key, value = item.split('*')
        if key in result:
            result[key] += float(value)
        else:
            result[key] = float(value)
    return [(key, value) for key, value in result.items()]


### EXAMPLE USAGE ####
example = False
if example:
    recipes = {"steel": ["iron*1", "match*1"], "match": ["stick*1", "coal*.25"], "stick": ["wood*0.25"]}
    inventory = {"tools": ["pickaxe", "wrench", "shovel"], "items": {"iron": 2, "match": 2, "wood": 2, "coal": 0.25}}
    all_ressources = ["wood", "stone", "iron", "metal", "coal", "steel plate", "rubber", "conveyor belt"]
    needed_time = 0.25
    craft_item = craft_item(inventory, recipes, needed_time)
    if craft_item[1]:
        inventory = craft_item[0]
    else:
        print(craft_item[0])
    print(inventory)
