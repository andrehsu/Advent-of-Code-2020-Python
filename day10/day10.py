from functools import lru_cache

INPUT = open('input.txt').read().splitlines()
TEST = open('test.txt').read().splitlines()
TEST1 = open('test1.txt').read().splitlines()


def part1(inp: list[str]) -> None:
    jolts = parse_input(inp)
    ones = 0
    threes = 0
    for i in range(len(jolts) - 1):
        a, b = jolts[i: i + 2]
        if b - a == 1:
            ones += 1
        elif b - a == 3:
            threes += 1
    print(ones * threes)


def part2(inp: list[str]) -> None:
    jolts = parse_input(inp)
    
    print(distinct_ways(jolts))


def parse_input(inp: list[str]) -> tuple[int]:
    jolts: list[int] = sorted(map(int, inp))
    jolts = [0, *jolts, max(jolts) + 3]
    return tuple(jolts)


@lru_cache(maxsize=None)
def distinct_ways(jolts: tuple[int]) -> int:
    if len(jolts) == 2:
        return 1
    total_ways = 0
    first = jolts[0]
    for i in range(1, len(jolts)):
        jolt = jolts[i]
        if jolt - first > 3:
            break
        total_ways += distinct_ways(jolts[i:])
    
    return total_ways


# def distinct_ways_arrange(jolts: tuple[int]):
#     if len(jolts) == 2:
#         yield jolts
#     first = jolts[0]
#     for i in range(1, len(jolts)):
#         jolt = jolts[i]
#         if jolt - first > 3:
#             break
#
#         for sub_arrange in distinct_ways_arrange(jolts[i:]):
#             ret = first, *sub_arrange
#             yield ret


if __name__ == '__main__':
    print('Test 0:')
    part1(TEST)
    part2(TEST)
    print('Test 1:')
    part1(TEST1)
    part2(TEST1)
    print('Solution:')
    part1(INPUT)
    part2(INPUT)
