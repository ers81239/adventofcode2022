import logging


logging.basicConfig(level=logging.INFO)



class FsObject:
    def __init__(self, name, size=0, parent=None):
        self.name = name
        self.parent = parent
        self.size = size
        self.children = []
        self.children_size = 0

    def add_child(self, fs_object):
        logging.info(f"Adding {fs_object.name} to {self.name} with size {fs_object.size}")
        fs_object.parent = self
        self.children.append(fs_object)

        # Add size to self
        self.children_size += fs_object.size

        # Add size to parents
        parent = self.parent
        while parent:
            parent.children_size += fs_object.size
            parent = parent.parent

    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None

    def print_list(self, level=0):
        print(f"{level * ' '}{self.name}: size:{self.size} children_size:{self.children_size}")
        for child in self.children:
            child.print_list(level+1)


class Terminal:
    def __init__(self):
        self.cur_dir = FsObject("/")

    def process_ls_output(self, output):
        """
        expectation is that output is pairs of size/type label and name
        """
        for index in range(0, len(output)-1, 2):
            size_type = output[index]
            name = output[index + 1]
            if size_type == "dir":
                if self.cur_dir.get_child(name):
                    logging.warning(f"Received duplicate name {name} in {self.cur_dir.name}")
                else:
                    self.cur_dir.add_child(FsObject(name))
            else:
                if self.cur_dir.get_child(name):
                    logging.warning(f"Received duplicate name {name} in {self.cur_dir.name}")
                else:
                    size = int(size_type)
                    self.cur_dir.add_child(FsObject(name, size))


    def process_command(self, command_str):
        command = map(str.strip, command_str.split())
        if command[0] == "cd":
            self.change_dirs(command[1])
        elif command[0] == "ls":
            self.process_ls_output(command[1:])


    def change_dirs(self, new_dir_name):
        logging.info(f"changing from {self.cur_dir.name} to {new_dir_name}")
        if new_dir_name == "/":
            while self.cur_dir.parent:
                self.cur_dir = self.cur_dir.parent
        elif new_dir_name == "..":
            if self.cur_dir.parent:
                self.cur_dir = self.cur_dir.parent
            else:
                logging.warning("Tried to cd .. from root dir")
        else:
            child_dir = self.cur_dir.get_child(new_dir_name)
            if child_dir:
                self.cur_dir = child_dir
            else:
                logging.warning("Creating new dir in response to cd command!")
                child_dir = FsObject(new_dir_name)
                self.cur_dir.add_child(child_dir)
                self.cur_dir = child_dir
        logging.info(f"Changed to {self.cur_dir.name}")


with open("input.txt", "r") as f:
    input_str = f.read()

command_strs = input_str.split("$")

terminal = Terminal()

for command_str in command_strs:
    logging.info("Processing: " + command_str)
    if command_str[0:3] == " cd":
        new_dir = command_str[3:].strip()
        terminal.change_dirs(new_dir)
    elif command_str[0:3] == " ls":
        terminal.process_ls_output(command_str.split()[1:])

terminal.change_dirs("/")
terminal.cur_dir.print_list()

# Task is to find sum of all directories containing at most 100k in "size"
def sum_of_children_under_100k(cur_dir):
    total_size = 0
    if cur_dir.children_size < 100000:
        total_size += cur_dir.children_size
    for child in cur_dir.children:
        total_size  += sum_of_children_under_100k(child)
    return total_size


print(f"Sum of children under 100k: {sum_of_children_under_100k(terminal.cur_dir)}")

terminal.change_dirs("/")


def emit_child_sizes_over(cur_dir, size):
    ret_val = []
    if cur_dir.children_size > size:
        ret_val.append(cur_dir.children_size)
    for child in cur_dir.children:
        ret_val.extend(emit_child_sizes_over(child, size))
    return ret_val

larger_than = 8381165

all_sizes = emit_child_sizes_over(terminal.cur_dir, larger_than)
all_sizes.sort()

for size in all_sizes:
    if size > larger_than:
        print(f"Smallest size over {larger_than} is {size}")
        break







