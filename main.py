from commands.go_to import go_to
from commands.mine import mine
from commands.craft_item import craft_item
from commands.create_item import create_item
from commands.get_item_dev import get_item_dev
from commands.repair import repair
import json


class ItemManufactory:
    def __init__(self):
        self.instruction = "comming lol"
        self.printing_pretty = True
        self.distance = 12
        self.needed_time_to_craft = 0.25
        self.needed_time_to_mine = 0.25
        self.inp = ""
        self.file_paths = {
            "upgrade_tiers_tools": "GameData/upgrade_tiers_tools.json",
            "upgrade_tiers_factorys": "GameData/upgrade_tiers_factorys.json",
            "all_ressources": "GameData/all_ressources.json",
            "recipes": "GameData/recipes.json",
            "inventory": "GameData/inventory.json",
            "player_experience": "GameData/player_experience.json",
            "positions": "GameData/positions.json"
        }

        self.commands = {"craft item": craft_item,
                         "create item": create_item,
                         "mine": mine,
                         "get item dev": get_item_dev,
                         "go to": go_to,
                         "repair tool": repair
                         }

        self.info_commands = ["save", "exit", "get pos", "get_inventory"]

    def get_command(self, inp):
        self.inp = inp
        if self.inp not in self.commands and self.inp not in self.info_commands:
            print(f"Command: {self.inp} doesn't exist!")
            self.game_loop()
            return

        if self.inp in self.commands:
            self.handle_command(self.inp)

        if self.inp in self.info_commands:
            self.handle_info_command(self.inp)

        self.game_loop()

    def handle_command(self, command):
        if command == "craft item":
            result = self.commands[command](inventory=self.inventory, recipes=self.recipes,
                                            needed_time_per_item=self.needed_time_to_craft)
            if not result[1]:
                print(result[0])
            else:
                self.inventory = result[0]
        if command == "mine":
            result = self.commands[command](inventory=self.inventory, pos=self.player_data.get("position"),
                                            mining_spots=self.positions.get("mining positions"), duarbility_tier=.5,
                                            needed_time_per_item=self.needed_time_to_mine)
            if not result[1]:
                print(result[0])
            else:
                self.inventory = result[0]
        elif command == "get item dev":
            self.inventory = get_item_dev(inventory=self.inventory)
        elif command == "repair tool":
            result = self.commands[command](inventory=self.inventory)
            if not result[1]:
                print(result[0])
            else:
                self.inventory = result[0]
        elif command == "go to":
            result = go_to(position=self.player_data.get("position"), possible_positions=self.positions.get("possible_positions"))
            if not result[1]:
                print(result[0])
            else:
                self.player_data["position"] = result[0]
                print(f"Your current position is: {self.player_data.get('position')}")

    def handle_info_command(self, command):
        if command == "save":
            self.save()
        elif command == "exit":
            self.save()
            exit()
        elif command == "get pos":
            print(f"Your current position is: {self.player_data.get('position')}")
        elif command == "get inventory":
            self.print_inventory_pretty()

    def game_loop(self):
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
            json.dump(self.inventory, f, indent=4)
        f.close()
        with open(self.file_paths.get("player_experience"), "w") as f:
            json.dump(self.player_data, f)
        f.close()

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
        # load player data
        self.player_data = self.load_json_file(file_path=self.file_paths.get("player_experience"))
        # laod positions
        self.positions = self.load_json_file(file_path=self.file_paths.get("positions"))

    def print_inventory_pretty(self):
        if self.printing_pretty:
            print(f"Tools:")
            for item, durability in self.inventory["tools"].items():
                print(f"\t- {item} Durability: {durability}")
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
