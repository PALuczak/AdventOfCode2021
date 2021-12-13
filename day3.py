buffer = [0,] * 12
with open("day3.txt", "r") as infile:
    for line in infile:
        for idx, val in enumerate(line.strip()):
            if val == "0":
                buffer[idx] -= 1
            elif val == "1":
                buffer[idx] += 1
            else:
                raise ValueError

gamma = sum((val > 0) << (11 - idx) for idx, val in enumerate(buffer))
epsilon = sum((val < 0) << (11 - idx) for idx, val in enumerate(buffer))

print("Part A", gamma, epsilon, gamma * epsilon)
