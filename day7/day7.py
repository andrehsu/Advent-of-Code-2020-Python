import re
from collections import deque

INPUT = open('input.txt').read().splitlines()
TEST = open('test.txt').read().splitlines()
TEST_2 = open('test2.txt').read().splitlines()


def parse_input(inp: list[str]) -> dict[str, dict[str, int]]:
    bags = {}
    for line in inp:
        owner, second = re.match(r'(\w+ \w+) bags contain (.+)', line).groups()
        
        children = {}
        if second != 'no other bags.':
            for bag_text in second.split(', '):
                tokens = bag_text.split()
                child_name = ' '.join(tokens[1:3])
    
                children[child_name] = int(tokens[0])
        
        bags[owner] = children
    return bags


def part1(inp: list[str]) -> None:
    bags = parse_input(inp)
    
    count = 0
    for owner in bags:
        q = deque([owner])
        while q:
            bag = q.popleft()
            children = bags[bag]
    
            if 'shiny gold' in children:
                count += 1
                break
    
            q.extend(children)
    
    print(count)


def part2(inp: list[str]) -> None:
    bags = parse_input(inp)
    total_count = 0
    q = deque(['shiny gold'])
    while q:
        bag = q.popleft()
        for child, count in bags[bag].items():
            total_count += count
            q.extend([child] * count)
    
    print(total_count)


if __name__ == '__main__':
    print('TESTS:')
    part1(TEST)
    part2(TEST)
    part2(TEST_2)
    print()
    print('SOLUTIONS:')
    part1(INPUT)
    part2(INPUT)
