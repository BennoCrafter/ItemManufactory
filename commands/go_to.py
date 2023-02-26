def go_to(position, possible_positions):
    wanted_pos = input("Where do you want to go?(iron source):")
    if wanted_pos in possible_positions:
        return wanted_pos, True
    else:
        return f"This position point does'nt exists! You can try:{possible_positions}", False
