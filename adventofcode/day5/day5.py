from itertools import combinations

INPUT = open('input.txt').read().splitlines()


def part1(inp: list[str]) -> None:
    print(max(map(calc_id, [decode(row) for row in inp])))


def part2(inp: list[str]) -> None:
    ids = set(map(calc_id, [decode(row) for row in inp]))
    for i, j in combinations(ids, 2):
        mid = None
        if (j - i == 2) and (mid := (i + j) // 2) not in ids:
            print(mid)


def decode(row) -> (int, int):
    row_hi = 128
    row_lo = 0
    for char in row[:7]:
        if char == 'F':
            row_hi = (row_hi + row_lo) // 2
        else:
            row_lo = (row_hi + row_lo) // 2
    
    col_hi = 8
    col_lo = 0
    for char in row[7:]:
        if char == 'L':
            col_hi = (col_hi + col_lo) // 2
        else:
            col_lo = (col_hi + col_lo) // 2
    
    return row_lo, col_lo


def calc_id(pos):
    r, c = pos
    return r * 8 + c


TESTS = open('tests.txt').read().splitlines()
if __name__ == '__main__':
    print("TESTS: ", end='')
    part1(TESTS)
    
    part1(INPUT)
    part2(INPUT)
