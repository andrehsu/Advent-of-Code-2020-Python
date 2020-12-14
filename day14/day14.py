import re
from collections import defaultdict
from typing import Generator

INPUT = open('input.txt').read().splitlines()
TEST = open('test.txt').read().splitlines()
TEST1 = open('test1.txt').read().splitlines()


def part1(inp: list[str]) -> None:
    mem = defaultdict(lambda: 0)
    or_mask = 0
    and_mask = 0
    for line in inp:
        if line.startswith('ma'):
            mask, = re.fullmatch(r'mask = ([X01]+)', line).groups()
            or_mask = int(mask.replace('X', '0'), 2)
            and_mask = int(mask.replace('X', '1'), 2)
        elif line.startswith('me'):
            pos, value = map(int, re.fullmatch(r'mem\[(\d+)] = (\d+)', line).groups())
            mem[pos] = (or_mask | value) & and_mask
        else:
            raise ValueError(line)
    
    print(sum(mem.values()))


def parse_addresses(mask: str, address: str) -> Generator[str, None, None]:
    if not mask:
        yield ''
    else:
        m, *m_rest = mask
        a, *a_rest = address
        for sub_address in parse_addresses(m_rest, a_rest):
            if m == '0':
                yield a + sub_address
            elif m == '1':
                yield '1' + sub_address
            else:
                yield '0' + sub_address
                yield '1' + sub_address


def part2(inp: list[str]) -> None:
    mem = defaultdict(lambda: 0)
    mask = ''
    for line in inp:
        if line.startswith('ma'):
            mask, = re.fullmatch(r'mask = ([X01]+)', line).groups()
        elif line.startswith('me'):
            address, value = map(int, re.fullmatch(r'mem\[(\d+)] = (\d+)', line).groups())
            address_bin = bin(address)[2:]
            address_bin = address_bin.zfill(len(mask))
            for address in parse_addresses(mask, address_bin):
                mem[int(address, 2)] = value
        else:
            raise ValueError(line)
    print(sum(mem.values()))


if __name__ == '__main__':
    print('Test:')
    part1(TEST)
    part2(TEST1)
    print('Solution:')
    part1(INPUT)
    part2(INPUT)
