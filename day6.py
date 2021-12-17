DAYS_A = 80
DAYS_B = 256

fishes = []
with open("day6.txt", "r") as infile:
    fishes = list(map(int, infile.read().strip().split(",")))

for day in range(DAYS_A):
    for i in range(len(fishes)):
        if fishes[i] == 0:
            fishes[i] = 6
            fishes.append(8)
        else:
            fishes[i] -= 1

print("Part A", len(fishes))

fishes = []
with open("day6.txt", "r") as infile:
    fishes = list(map(int, infile.read().strip().split(",")))
stage_cnt = 9
stages = [0] * stage_cnt
for fish in fishes:
    stages[fish] += 1

for day in range(DAYS_B):
    new_fishes = stages[0]
    for i in range(0, stage_cnt - 1):
        stages[i] = stages[i + 1]
    stages[8] = new_fishes
    stages[6] += new_fishes

print("Part B", sum(stages))
