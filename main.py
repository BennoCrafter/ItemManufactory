from commands.mine import mine
from commands.craft_item import craft_item
from commands.create_item import create_item
from commands.get_item_dev import get_item_dev
import json


class ItemManufactory:
    def __init__(self):
        self.instruction = "comming lol"
        self.printing_pretty = True
        self.inp = ""
        self.file_paths = {
            "upgrade_tiers_tools": "GameData/upgrade_tiers_tools.json",
            "upgrade_tiers_factorys": "GameData/upgrade_tiers_factorys.json",
            "all_ressources": "GameData/all_ressources.json",
            "recipes": "GameData/recipes.json",
            "inventory": "GameData/inventory.json",
            "player_experience": "GameData/player_experience.json"
        }

        self.commands = {"craft item": craft_item,
                         "create item": create_item,
                         "mine": mine,
                         "get item dev": get_item_dev,
                         "save": "placeholder",
                         "exit": "placeholder"}

    def get_command(self, inp):
        self.inp = inp
        if self.inp in self.commands.keys():
            if self.inp == "save":
                self.save()
            elif self.inp == "exit":
                self.save()
                exit()
            else:
                new_inventory = self.commands[self.inp](inventory=self.inventory, ressources=self.ressources, recipes=self.recipes)
                if new_inventory[1]:
                    self.inventory = new_inventory[0]
                else:
                    print(new_inventory[0])
        else:
            print(f"Command: {self.inp} does'nt exists!")
        self.game_loop()

    def game_loop(self):
        self.print_inventory_pretty()
        self.get_command(inp=input("Input:"))

    def print_instruction(self):
        print("Instruction...")
        print(self.instruction)

    def load_json_file(self, file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
        return data

    def save(self):
        with open(self.file_paths.get("inventory"), "w") as f:
            json.dump(self.inventory, f)

    def load_game_data(self):
        # load upgrade_tiers
        self.upgrade_tiers_tools = self.load_json_file(file_path=self.file_paths.get("upgrade_tiers_tools"))
        self.upgrade_tiers_factorys = self.load_json_file(file_path=self.file_paths.get("upgrade_tiers_factorys"))
        # load ressources
        self.ressources = self.load_json_file(file_path=self.file_paths.get("all_ressources"))
        # load inventory
        self.inventory = self.load_json_file(file_path=self.file_paths.get("inventory"))
        # load recipes
        self.recipes = self.load_json_file(file_path=self.file_paths.get("recipes"))

    def print_inventory_pretty(self):
        if self.printing_pretty:
            print(f"Tools:")
            for item in self.inventory["tools"]:
                print(f"\t- {item}")
            print(f"Items:")
            for item, count in self.inventory["items"].items():
                print(f"\t- {item}:{count}")
        else:
            print(self.inventory)


if __name__ == "__main__":
    item_manufactory = ItemManufactory()
    item_manufactory.load_game_data()
    item_manufactory.print_instruction()
    item_manufactory.game_loop()
