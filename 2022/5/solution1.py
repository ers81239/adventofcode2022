from collections import namedtuple
import logging

Command = namedtuple("Command", ["count", "from_stack", "to_stack"])


logging.basicConfig(level=logging.INFO)

class Ship:
    def __init__(self, stacks: list = None):

        # the bottom of the stack is index 0
        if stacks:
            self.stacks = stacks
        else:
            self.stacks = []

    def execute_command(self, command: Command):
        logging.info(f"Processing command: {command}")
        for i in range(command.count):
            self.move_container(command.from_stack, command.to_stack)

    def move_container(self, from_stack, to_stack):
        logging.info(f"Moving container from {from_stack} to {to_stack}")
        crate = self.stacks[from_stack].pop()
        self.stacks[to_stack].append(crate)


def read_input(filename):
    stacks = []
    commands = []

    with open(filename, "r") as f:
        lines = f.readlines()

    def load_stacks(stacks_text_list):

        """
        Sample stack input:
            [H]         [H]         [V]
            [V]         [V] [J]     [F] [F]
            [S] [L]     [M] [B]     [L] [J]
            [C] [N] [B] [W] [D]     [D] [M]
        [G] [L] [M] [S] [S] [C]     [T] [V]
        [P] [B] [B] [P] [Q] [S] [L] [H] [B]
        [N] [J] [D] [V] [C] [Q] [Q] [M] [P]
        [R] [T] [T] [R] [G] [W] [F] [W] [L]
         1   2   3   4   5   6   7   8   9

        Procedure:
        1. Loop backwards, populating each list as you go

        Consider that an entire stack could be empty
        just keep the delimiters as part of the crate identifier
        """

        stack_count = int(stacks_text_list[-1].split()[-1])
        stacks = [[] for stack in range(stack_count)]

        lines = reversed(stacks_text_list[:-1])
        for line_index, line in enumerate(lines):
            pos = 0  # string position index, start at 1 as it is the start of first crate
            for stack_index in range(stack_count):
                # read a single crate from the line
                crate = line[pos:pos+3].strip()
                if crate:
                    stacks[stack_index].append(crate)
                pos += 4

        return stacks

    def load_commands(commands_text_list):
        """
        sample command input:
          move 3 from 3 to 7
          move 4 from 1 to 9
          move 5 from 6 to 3
          move 6 from 9 to 8
        """
        commands = []
        for line in commands_text_list:
            words = line.split()
            command = Command(
                count = int(words[1]),
                from_stack = int(words[3]) - 1,
                to_stack = int(words[5]) - 1
            )
            commands.append(command)
        return commands

    for index, line in enumerate(lines):
        if not line.strip():
            first_blank_line_index = index
            break

    stacks = load_stacks(lines[:first_blank_line_index])

    commands = load_commands(lines[first_blank_line_index + 1:])

    return stacks, commands


stacks, commands = read_input("input.txt")

ship = Ship(stacks)

for command in commands:
    ship.execute_command(command)

# Print the top of each stack
for stack in ship.stacks:
    print(stack[-1:])
    HBTMTBSDC