from operator import itemgetter

INPUT = open('input.txt').read().splitlines()
TEST = open('TEST.txt').read().splitlines()


def part1(inp: list[str]) -> None:
    earliest = int(inp[0])
    buses = [int(i) for i in inp[1].split(',') if i != 'x']
    deltas = []
    for bus in buses:
        departs = (earliest // bus + 1) * bus
        deltas.append((bus, departs - earliest))
    
    soonest = min(deltas, key=itemgetter(1))
    print(soonest[0] * soonest[1])


def part2(inp: list[str]) -> None:
    """
    Put resulting string into Wolfram Alpha or another system of equations solver
    :param inp: input for the puzzle
    :return: None
    """
    buses = inp[1].split(',')
    equations = []
    for i, bus in enumerate(buses):
        if bus == 'x':
            continue
        equations.append(f'(t+{i}) mod {bus} = 0')
    print(','.join(equations))


if __name__ == '__main__':
    print('Test:')
    part1(TEST)
    part2(TEST)
    print('Solution:')
    part1(INPUT)
    part2(INPUT)
