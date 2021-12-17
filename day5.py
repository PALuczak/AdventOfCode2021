# should be smaller than a NxN matrix
diagonal = True

scores = dict()  # : dict[tuple[int,int],[int]] # (X, Y), overlaps
with open("day5.txt", "r") as infile:
    for line in infile:
        start, stop = line.split("->")
        x1, y1 = [int(val) for val in start.strip().split(",")]
        x2, y2 = [int(val) for val in stop.strip().split(",")]
        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))

        if x1 == x2:
            for y in range(y1, y2 + 1):
                scores[(x1, y)] = scores.get((x1, y), 0) + 1
        elif y1 == y2:
            for x in range(x1, x2 + 1):
                scores[(x, y1)] = scores.get((x, y1), 0) + 1
        elif diagonal:
            # at 45 degrees the number of X and Y steps should be equal
            for x, y in zip(range(x1, x2 + 1), range(y1, y2 + 1)):
                scores[(x, y)] = scores.get((x, y), 0) + 1

two_count = 0
for val in scores.values():
    if val >= 2:
        two_count += 1

print(f"Part {'B' if diagonal else 'A'}", two_count)

# 4421
# 18674
