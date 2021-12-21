simple_digits = 0


def is_simple(digit):
    return len(digit) in {2, 3, 4, 7}


with open("day8.txt", "r") as infile:
    for line in infile:
        patterns, outputs = line.split("|")
        patterns = patterns.split()
        outputs = outputs.split()
        for output in outputs:
            simple_digits += int(is_simple(output))


print("Part A ", simple_digits)
