with open("input.txt", "r") as f:
    lines = f.read().splitlines()

elf_cals = []  # index is elf number, value is calorie total
elf_id = 0 # The index of the current elf
max_cals = -1
max_cal_elf = None

for line_no, line in enumerate(lines):
    if line_no == 0:
        elf_cals.append(0)

    if line.strip() == "":
        # this is a new elf
        if elf_cals[elf_id] > max_cals:
            # set a new champion
            max_cal_elf = elf_id
            max_cals = elf_cals[elf_id]
        elf_id += 1
        elf_cals.append(0)

    else:
        # this is a calorie line for the current elf
        elf_cals[elf_id] += int(line.strip())

print(f"Greatest calories is on elf {max_cal_elf} with {max_cals}.")
#print(f"Here is the list: {',  '.join([f'{num}: {cals}' for num, cals in enumerate(elf_cals)])}")

# part 2

sorted_cals = sorted(elf_cals, reverse=True)
print(sorted_cals)
print(f"Top 3 elves have {sum(sorted_cals[:3])} calories")

