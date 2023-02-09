from commands.mine import mine
from commands.craft_item import craft_item
from commands.create_item import create_item
from commands.get_item_dev import get_item_dev


class ItemManufactory:
    def __init__(self):
        self.instruction = "comming lol"
        self.inp = ""
        self.file_paths = {
            "upgrade_tiers_tools": "GameData/upgrade_tiers_tools.json",
            "upgrade_tiers_factorys": "GameData/upgrade_tiers_factorys.json",
            "all_raw_ressources": "GameData/all_raw_ressources.json",
            "all_ressources": "GameData/all_ressources.json",
            "recipes": "GameData/recipes.json",
            "inventory": "GameData/inventory.json",
            "player_experience": "GameData/player_experience.json"
        }

        self.upgrade_tiers_tools = ["Basic", "Durability", "Ergonomic", "Performance", "Material", "Blade", "Power", "Multifunction"]
        self.upgrade_tiers_factorys = ["Basic", "Automation", "Energy Efficiency"]
        self.all_raw_ressources = ["wood", "stone", "iron", "coal", "rubber", "cotton"]
        self.all_ressources = ["wood", "stone", "iron", "metal", "coal", "steel plate", "rubber", "conveyor belt"]
        self.commands = {"craft item": craft_item,
                         "create item": create_item,
                         "mine": mine,
                         "get item dev": get_item_dev}

        self.recipes = {"metal*1": ["iron*1", "match*1"], "match*4": ["stick*4", "coal*1"], "stick*4": ["wood*1"]}
        self.inventory = {"tools": ["pickaxe", "wrench", "shovel"], "items": {}}
        self.upgrades = {"tools": {"pickaxe": self.upgrade_tiers_tools[0], "wrench": self.upgrade_tiers_tools[0], "shovel": self.upgrade_tiers_tools[0]}, "factorys": {"Starter factory": self.upgrade_tiers_factorys[0]}}
        print(self.upgrades.get("tools").get("pickaxe"))

    def get_command(self, inp):
        self.inp = inp
        if self.inp in self.commands.keys():
            self.inventory = self.commands[self.inp](inventory=self.inventory, all_ressources=self.all_ressources, recipes=self.recipes)
        else:
            print(f"Command: {self.inp} does'nt exists!")
        self.game_loop()

    def game_loop(self):
        print(self.inventory)
        self.get_command(inp=input("Input:"))

    def print_instruction(self):
        print("Instruction...")
        print(self.instruction)

    def load_game_data(self):
        pass


if __name__ == "__main__":
    item_manufactory = ItemManufactory()
    item_manufactory.print_instruction()
    item_manufactory.game_loop()
