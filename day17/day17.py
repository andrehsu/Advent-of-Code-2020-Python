from itertools import product

import numpy as np

INPUT = open('input.txt').read().splitlines()
TEST = open('test.txt').read().splitlines()


def part1(inp: list[str]) -> None:
    length = len(inp) + (1 + 6) * 2  # 1 for padding, 6 for steps, 2 for both sides
    space = np.zeros((length,) * 3, dtype=int)
    offset = length // 2 - len(inp) // 2
    space[offset, offset: offset + len(inp), offset: offset + len(inp[0])] = np.array(
        [list(i == '#' for i in row) for row in inp])
    for i in range(6):
        new_space = np.zeros_like(space)
        for x, y, z in product(range(1, length - 1), repeat=3):
            if space[x, y, z] == 1:
                count = space[x - 1:x + 2, y - 1:y + 2, z - 1:z + 2].sum() - 1
                if count == 2 or count == 3:
                    new_space[x, y, z] = 1
            else:
                count = space[x - 1:x + 2, y - 1:y + 2, z - 1:z + 2].sum()
                if count == 3:
                    new_space[x, y, z] = 1
        space = new_space
    
    print(space.sum())


def part2(inp: list[str]) -> None:
    length = len(inp) + (1 + 6) * 2  # 1 for padding, 6 for steps, 2 for both sides
    space = np.zeros((length,) * 4, dtype=int)
    offset = length // 2 - len(inp) // 2
    space[offset, offset, offset: offset + len(inp), offset: offset + len(inp[0])] = np.array(
        [list(i == '#' for i in row) for row in inp])
    for i in range(6):
        new_space = np.zeros_like(space)
        for x, y, z, w in product(range(1, length - 1), repeat=4):
            if space[x, y, z, w] == 1:
                count = space[x - 1:x + 2, y - 1:y + 2, z - 1:z + 2, w - 1:w + 2].sum() - 1
                if count == 2 or count == 3:
                    new_space[x, y, z, w] = 1
            else:
                count = space[x - 1:x + 2, y - 1:y + 2, z - 1:z + 2, w - 1:w + 2].sum()
                if count == 3:
                    new_space[x, y, z, w] = 1
        space = new_space
    
    print(space.sum())


if __name__ == '__main__':
    part1(TEST)
    part2(TEST)
    part1(INPUT)
    part2(INPUT)
