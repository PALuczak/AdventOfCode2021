prev = -1
increases = 0
with open("day1.txt", "r") as infile:
    for line in infile:
        val = int(line)
        if prev != -1 and val > prev:
            increases += 1
        prev = val

print("PART A", increases)
