def get_recipe(inventory, recipes):
    split_element = "*"
    inp = input("Please enter item from what you want the recipe (insulator*3):")
    if split_element in inp:
        item_for_recipe, count = inp.split("*")
    else:
        item_for_recipe, count = inp, 1

    all_craftable_things = {}
    ressources_for_crafting = {}
    pretty_ressources = "Needed Ressources:\n\n"
    # get all craftable items in a dictonary -> key = repair tool -- value = tool
    for item in recipes.keys():
        all_craftable_things[item.split("|")[0]] = item.split("|")[1]
    # get recipe for user's item
    recipe = recipes.get(item_for_recipe + "|" + all_craftable_things.get(item_for_recipe))
    if item_for_recipe in all_craftable_things.keys():
        for item in recipe:
            ressources_for_crafting[item.split("*")[0]] = int(item.split("*")[1]) * int(count)
        # save ressources pretty
        for item, count in ressources_for_crafting.items():
            pretty_ressources += f"- {item}: {count}\n"
        return pretty_ressources
    else:
        return "This Item doesn't exists!"


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
    print(get_recipe(inventory, recipes))
