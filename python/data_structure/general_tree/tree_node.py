class TreeNode:
    PRINT_OPTION = {
        "NAME": "name",
        "POSITION": "position",
    }

    TEXT_SPACE = " "

    def __init__(self, data):
        self.data = data
        self.child = []
        self.parent = None
        self.level = 0

    def add_child(self, child):
        child.parent = self
        self.child.append(child)

    def get_level(self):
        level = 0
        node_parent = self.parent
        
        while(node_parent):
            level += 1
            node_parent = node_parent.parent

        return level

    def print_data_by(self, print_option=None):
        level = self.get_level()
        prefix = f"""{"  " * level} {"|-- " if level != 0 else ""}"""
        print_pattern = f"""{self.data["name"]} [{self.data["position"]}]"""
        
        if print_option:
            self.PRINT_OPTION[print_option]
            print_pattern = f"""{self.data[self.PRINT_OPTION[print_option]]}"""
        
        print(prefix + f" [{level}] " + print_pattern)

        for child in self.child:
            child.print_data_by(print_option)
