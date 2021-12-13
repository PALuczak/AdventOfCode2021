prev = -1
increases = 0
with open("day1.txt", "r") as infile:
    for line in infile:
        val = int(line)
        if prev != -1 and val > prev:
            increases += 1
        prev = val

print("PART A", increases)

prev = -1
increases = 0
with open("day1.txt", "r") as infile:
    vals = [int(val) for val in infile]

    for x in zip(vals, vals[1:], vals[2:]):
        val = sum(x)
        if prev != -1 and val > prev:
            increases += 1
        prev = val
print("PART B", increases)
