def mine(inventory, pos, mining_spots, duarbility_tier):
    if pos in mining_spots:
        append_item_count = 1
        print(f"You're current position is: {pos}")
        tool_to_use = input(f"Which tool do you want to use for mining {pos.split(' ')[0]}?:")
        count = int(input("How often do you want to mine?:"))
        if tool_to_use in inventory["tools"].keys():
            item, art = pos.split(" ")
            # check if user has the matching tool
            if art == "tree":
                if tool_to_use != "axe":
                    return "You're using the wrong Tool", False
            elif art == "source":
                if tool_to_use != "pickaxe":
                    return "You're using the wrong Tool", False

            # shrink durability of tool
            inventory["tools"][tool_to_use] -= float(duarbility_tier)
            # append new item to dict
            if item in inventory["items"].keys():
                inventory["items"][item] += append_item_count * count
            else:
                inventory["items"][item] = append_item_count * count
            return inventory, True
        else:
            return "You don't have the tool!", False

    else:
        return "You're not on a mining spot!", False
