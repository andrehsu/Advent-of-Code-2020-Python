from copy import deepcopy

INPUT = open('input.txt').read().splitlines()
TEST = open('test.txt').read().splitlines()


def part1(inp: list[str]) -> None:
    layout = [list(row) for row in inp]
    seen = set()
    while True:
        new_layout = deepcopy(layout)
        for i, row in enumerate(layout):
            for j in range(len(row)):
                count = count_visible(layout, i, j, 1)
                if count == 0 and layout[i][j] == 'L':
                    new_layout[i][j] = '#'
                elif count >= 4 and layout[i][j] == '#':
                    new_layout[i][j] = 'L'
        
        layout = new_layout
        key = tuple(tuple(row) for row in layout)
        if key in seen:
            break
        seen.add(key)
    print(sum(sum(i == '#' for i in row) for row in layout))


def print_layout(layout: list[list[str]]):
    for row in layout:
        print(''.join(row))
    print()


def part2(inp: list[str]) -> None:
    layout = [list(row) for row in inp]
    seen = set()
    while True:
        new_layout = deepcopy(layout)
        for i, row in enumerate(layout):
            for j in range(len(row)):
                count = count_visible(layout, i, j)
                if count == 0 and layout[i][j] == 'L':
                    new_layout[i][j] = '#'
                elif count >= 5 and layout[i][j] == '#':
                    new_layout[i][j] = 'L'
        
        layout = new_layout
        key = tuple(tuple(row) for row in layout)
        if key in seen:
            break
        seen.add(key)
    print(sum(sum(i == '#' for i in row) for row in layout))


def count_visible(layout: list[list[str]], i: int, j: int, max_radius=9999):
    deltas = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    count = 0
    radius = 1
    while deltas and radius <= max_radius:
        new_deltas = []
        for delta in deltas:
            d_i, d_j = delta
            i_ = i + (d_i * radius)
            j_ = j + (d_j * radius)
            if 0 <= i_ < len(layout) and 0 <= j_ < len(layout[i_]):
                loc = layout[i_][j_]
                if loc == '.':
                    new_deltas.append(delta)
                    continue
                if loc == '#':
                    count += 1
        deltas = new_deltas
        radius += 1
    
    return count


if __name__ == '__main__':
    print('Test:')
    part1(TEST)
    part2(TEST)
    print('Solution:')
    part1(INPUT)
    part2(INPUT)
