with open("input.txt", "r") as f:
    data = f.read()


def has_repeats(s):
    s_sorted = sorted(s)
    for char_no, char in enumerate(s_sorted):
        if char_no > 0:
            if char == s_sorted[char_no-1]:
                return True
    return False


def find_first_no_repeats(data, length = 4):
    for char_no, char in enumerate(data):
        if char_no < length:
            pass
        else:
            if not has_repeats(data[char_no-length:char_no]):
                return char_no
    return -1

start = find_first_no_repeats(data)
print(start)

first_msg = find_first_no_repeats(data, length=14)
print(first_msg)