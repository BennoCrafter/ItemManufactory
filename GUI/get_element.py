class Gui:
    def __init__(self):
        self.map = ""

    def get_right_gui_element(self, inp, inventory, specific_pos):
        if inp == "get pos":
            little_map = self.map[specific_pos[1]-2:specific_pos[1]+2]
            for line in little_map:
                print(line)

    def load_map(self):
        with open("GUI/map.txt", "r") as file:
            self.map = file.read().split("\n")
        # for line in self.map:
        #     print(line)


if __name__ == "__main__":
    gui = Gui()
    gui.load_map()
    gui.get_right_gui_element(inp="get pos", inventory=None, specific_pos=[10,10])
