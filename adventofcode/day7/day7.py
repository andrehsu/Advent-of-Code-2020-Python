import re
from collections import deque

INPUT = open('input.txt').read().splitlines()
TEST = open('test.txt').read().splitlines()
TEST_2 = open('test2.txt').read().splitlines()

pattern = r'\w+_\w+'


def parse_input(inp: list[str]) -> dict[str, dict[str, int]]:
    bags = {}
    for line in inp:
        first, second = line.split(' contain ')
        owner = '_'.join(first.split()[:2])
        assert owner not in bags, f'{owner} already in bags'
        assert re.match(pattern, owner), owner
        
        children = {}
        if second != 'no other bags.':
            for bag_text in second.split(', '):
                tokens = bag_text.split()
                child_name = '_'.join(tokens[1:3])
                assert re.match(pattern, child_name), child_name
                
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
            
            if 'shiny_gold' in children:
                count += 1
                break
            
            q.extend(children)
    
    print(count)


def part2(inp: list[str]) -> None:
    bags = parse_input(inp)
    total_count = 0
    q = deque(['shiny_gold'])
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
