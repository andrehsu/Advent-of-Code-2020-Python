from collections import Counter, deque

INPUT = open('input.txt').read().splitlines()
TEST = open('test.txt').read().splitlines()


def part1(inp: list[str]) -> None:
    q = deque(inp)
    count = 0
    while q:
        yes = set()
        while q:
            row = q.popleft()
            if row == '':
                break
            for c in row:
                yes.add(c)
        count += len(yes)
    
    print(count)


def part2(inp: list[str]) -> None:
    q = deque(inp)
    count = 0
    while q:
        yes = Counter()
        rows = 0
        while q:
            row = q.popleft()
            if row == '':
                break
            rows += 1
            for c in row:
                yes[c] += 1
        all_yes = 0
        for k, v in yes.items():
            if v == rows:
                all_yes += 1
        
        count += all_yes
    
    print(count)


if __name__ == '__main__':
    print('TEST:')
    part1(TEST)
    part2(TEST)
    print('ACTUAL:')
    part1(INPUT)
    part2(INPUT)
