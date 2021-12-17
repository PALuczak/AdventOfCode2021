crabs = []  # list[int]
with open("day7.txt", "r") as infile:
    crabs = list(map(int, infile.read().strip().split(",")))

fuel = []
for pos in range(max(crabs)):
    fuel.append(sum(abs(crab - pos) for crab in crabs))

print("Part A", min(fuel))

fuel = []
for pos in range(max(crabs)):
    # sum of arithmetic progresson
    fuel.append(
        sum(
            (abs(crab - pos) * (abs(crab - pos) + 1)) // 2
            for crab in crabs
            if abs(crab - pos)
        )
    )

print("Part B", min(fuel))
