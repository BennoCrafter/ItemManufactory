def repair(inventory):
    repair_kit_name = "repair kit"
    if repair_kit_name in inventory["tools"].keys():
        tool_to_repair = input("Which tool do you want to repair?:")
        if tool_to_repair in inventory["tools"].keys():
            durability = inventory["tools"].get(tool_to_repair)
            durability_to_repair = 100 - durability
            # append durability to tool
            inventory["tools"][tool_to_repair] += durability_to_repair
            # shrink durability of repair kit
            inventory["tools"][repair_kit_name] -= float(durability_to_repair/4)
            print(f"Repaired {tool_to_repair} successfully!")
            return inventory, True
        else:
            return f"The item {tool_to_repair} does'nt exists!", False
    else:
        return "You have no repair kit!", False
