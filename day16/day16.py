import re
import time
from functools import lru_cache
from typing import NamedTuple
from typing import TypeVar

INPUT = open('input.txt').read().splitlines()
TEST = open('test.txt').read().splitlines()
TEST1 = open('test1.txt').read().splitlines()


class Field(NamedTuple):
    name: str
    a: int
    b: int
    c: int
    d: int


Ticket = tuple[int, ...]


def part1(inp: list[str]) -> None:
    fields, your_ticket, tickets = parse_input(inp)
    _, error_rate = filter_tickets(fields, tickets)
    print(error_rate)


def part2(inp: list[str]) -> None:
    @lru_cache(maxsize=None)
    def is_valid_field(field: Field, i: int) -> bool:
        _, a, b, c, d = field
        for ticket in tickets:
            value = ticket[i]
            if not (a <= value <= b or c <= value <= d):
                return False
        
        return True
    
    @lru_cache(maxsize=None)
    def recurse(remaining_fields: tuple[Field], i=0) -> list[list[Field]]:
        if not remaining_fields:
            return [[]]
        else:
            ret = []
            for field in remaining_fields:
                if is_valid_field(field, i):
                    for sub_solution in recurse(tuple_without(remaining_fields, field), i + 1):
                        ret.append([field] + sub_solution)
            return ret
    
    fields, your_ticket, tickets = parse_input(inp)
    tickets, _ = filter_tickets(fields, tickets)
    valid_permutations = recurse(tuple(fields))
    result = 1
    for field, value in zip(valid_permutations[0], your_ticket):
        if field.name.startswith('departure'):
            result *= value
    
    print(result)


T = TypeVar('T')


def tuple_without(l: tuple[T], without: T) -> tuple[T]:
    l = list(l)
    l.remove(without)
    return tuple(l)


def parse_input(inp: list[str]) -> tuple[list[Field], Ticket, list[Ticket]]:
    it = iter(inp)
    
    fields = []
    for line in it:
        if line == '':
            break
        name, *nums = re.fullmatch(r'([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)', line).groups()
        a, b, c, d = map(int, nums)
        field = Field(name, a, b, c, d)
        fields.append(field)
    
    next(it)
    your_ticket = ()
    for line in it:
        if line == '':
            break
        your_ticket = tuple(map(int, line.split(',')))
    
    next(it)
    tickets = []
    for line in it:
        tickets.append(tuple(map(int, line.split(','))))
    
    return fields, your_ticket, tickets


def is_valid_value(fields: list[Field], value: int):
    for field in fields:
        _, a, b, c, d = field
        if a <= value <= b or c <= value <= d:
            return True
    return False


def filter_tickets(fields: list[Field], tickets: list[Ticket]) -> tuple[list[Ticket], int]:
    error_rate = 0
    valid_tickets = []
    for ticket in tickets:
        is_valid_ticket = True
        for value in ticket:
            if not is_valid_value(fields, value):
                error_rate += value
                is_valid_ticket = False
        if is_valid_ticket:
            valid_tickets.append(ticket)
    return valid_tickets, error_rate


if __name__ == '__main__':
    # print('Test:')
    # part1(TEST)
    # part2(TEST1)
    # print('Solution:')
    # part1(INPUT)
    start = time.time()
    part2(INPUT)
    end = time.time()
    print(f'Elapsed: {end - start:.3f}')
