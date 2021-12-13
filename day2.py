horizontal = 0
depth = 0
with open("day2.txt", "r") as infile:
    for line in infile:
        dir, val = line.split()
        val = int(val)
        if dir == "forward":
            horizontal += val
        elif dir == "down":
            depth += val
        elif dir == "up":
            depth -= val
        else:
            raise ValueError

print("Part A", horizontal, depth, horizontal * depth)

horizontal = 0
depth = 0
aim = 0
with open("day2.txt", "r") as infile:
    for line in infile:
        dir, val = line.split()
        val = int(val)
        if dir == "forward":
            horizontal += val
            depth += aim * val
        elif dir == "down":
            aim += val
        elif dir == "up":
            aim -= val
        else:
            raise ValueError

print("Part B", horizontal, depth, horizontal * depth)
