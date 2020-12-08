INPUT = list(map(int, open('input.txt').read().splitlines()))


def part1(inp: list[int]) -> None:
    for i in range(len(inp)):
        for j in range(i + 1, len(inp)):
            if i != j and inp[i] + inp[j] == 2020:
                print(inp[i] * inp[j])
                return


def part2(inp: list[int]) -> None:
    for i in range(len(inp)):
        for j in range(i + 1, len(inp)):
            for k in range(j + 1, len(inp)):
                if len({i, j, k}) == 3 and inp[i] + inp[j] + inp[k] == 2020:
                    print(inp[i] * inp[j] * inp[k])
                    return


if __name__ == '__main__':
    part1(INPUT)
    part2(INPUT)
