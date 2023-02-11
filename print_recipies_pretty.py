import json


class Recipes:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        with open(self.filename, "r") as file:
            self.data = json.load(file)

    def print_data_pretty(self):
        for craftable_item in self.data.keys():
            needed_items = ""
            for item in self.data.get(craftable_item):
                needed_items += f"{item}  "
            print(f"Item: {craftable_item}  Ressources: {needed_items}")


if __name__ == "__main__":
    recipe_object = Recipes(filename="GameData/recipes.json")
    recipe_object.read_data()
    recipe_object.print_data_pretty()
