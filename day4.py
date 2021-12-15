import numpy as np

numbers = []  # : list[int]
scores = []  # : list[tuple[int,int]]
with open("day4.txt", "r") as infile:
    numbers = [int(val) for val in infile.readline().split(",")]
    infile.readline()  # skip the empty line
    board = np.zeros((5, 5))
    rdx = 0
    for line in infile:
        line = line.strip()
        if not line:
            board_mask = np.zeros_like(board)
            for idx, num in enumerate(numbers):
                board_mask += board == num
                if (np.array([*board_mask.sum(0), *board_mask.sum(1)]) == 5).any():
                    score = int(np.sum(board * (1 - board_mask)) * num)
                    if score:
                        scores.append((idx, score))
                        break
            rdx = 0
            continue

        line = [int(val) for val in line.split()]
        board[rdx] = line
        rdx += 1

scores = sorted(scores)

print("Part A", scores[0])
print("Part B", scores[-1])
