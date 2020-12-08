INPUT = open('input.txt').read().splitlines()


def part1(input_: list[str]) -> None:
    i = 0
    j = 0
    trees = 0
    while i < len(input_) - 1:
        i += 1
        j += 3
        if input_[i][j % len(input_[i])] == '#':
            trees += 1
    print(trees)


def part2(input_: list[str]) -> None:
    i = 0
    j = 0
    trees = 0
    while i < len(input_) - 1:
        i += 1
        j += 3
        if input_[i][j % len(input_[i])] == '#':
            trees += 1
    total = trees
    i = 0
    j = 0
    trees = 0
    while i < len(input_) - 1:
        i += 1
        j += 1
        if input_[i][j % len(input_[i])] == '#':
            trees += 1
    
    total *= trees
    
    i = 0
    j = 0
    trees = 0
    while i < len(input_) - 1:
        i += 1
        j += 5
        if input_[i][j % len(input_[i])] == '#':
            trees += 1
    total *= trees
    i = 0
    j = 0
    trees = 0
    while i < len(input_) - 1:
        i += 1
        j += 7
        if input_[i][j % len(input_[i])] == '#':
            trees += 1
    total *= trees
    
    i = 0
    j = 0
    trees = 0
    while i < len(input_) - 1:
        i += 2
        j += 1
        if input_[i][j % len(input_[i])] == '#':
            trees += 1
    total *= trees
    
    print(total)


if __name__ == '__main__':
    part1(INPUT)
    part2(INPUT)
