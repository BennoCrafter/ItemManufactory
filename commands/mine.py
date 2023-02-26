import time


def mine(inventory, pos, mining_spots, duarbility_tier, needed_time_per_item):
    if pos in mining_spots:
        append_item_count = 1
        print(f"You're current position is: {pos}")
        tool_to_use = input(f"Which tool do you want to use for mining {pos.split(' ')[0]}?:")
        if tool_to_use in inventory["tools"].keys():
            item, art = pos.split(" ")
            # check if user has the matching tool
            if art == "tree":
                if tool_to_use != "axe":
                    return "You're using the wrong Tool", False
            elif art == "source":
                if tool_to_use != "pickaxe":
                    return "You're using the wrong Tool", False
            elif art == "place":
                if tool_to_use != "shovel":
                    return "You're using the wrong Tool", False

            count = input("How often do you want to mine?:")
            if count.isdigit():
                count = int(count)
            else:
                return "Please enter a valid number!", False
            # shrink durability of tool
            inventory["tools"][tool_to_use] -= float(duarbility_tier) * count
            # append new item to dict
            if item in inventory["items"].keys():
                inventory["items"][item] += append_item_count * count
            else:
                inventory["items"][item] = append_item_count * count
            print(f"mining... Needed time: {needed_time_per_item*count}")
            time.sleep(needed_time_per_item*count)
            print("Finished!")
            return inventory, True
        else:
            return "You don't have the tool!", False

    else:
        return "You're not on a mining spot!", False
