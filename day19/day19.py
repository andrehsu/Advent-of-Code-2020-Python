import abc
import re

INPUT = open('input.txt').read().splitlines()
TEST = open('test.txt').read().splitlines()
TEST1 = open('test1.txt').read().splitlines()


class Pattern(abc.ABC):
    max_depth = 50
    
    @abc.abstractmethod
    def to_regex(self, rules: dict[int, 'Pattern'], depth: int) -> str:
        pass


class Value(Pattern):
    def __init__(self, value: str):
        self.value = value

    def to_regex(self, rules: dict[int, 'Pattern'], depth: int) -> str:
        return self.value


class Refs(Pattern):
    def __init__(self, ref_ids: list[int]):
        self.ref_ids = ref_ids
    
    def to_regex(self, rules: dict[int, 'Pattern'], depth: int) -> str:
        if depth == Pattern.max_depth:
            return 'x'
        sb = []
        for ref_id in self.ref_ids:
            sb.append(rules[ref_id].to_regex(rules, depth + 1))
        return '(' + ''.join(sb) + ')'
    
    @staticmethod
    def parse(s: str) -> 'Refs':
        return Refs(list(map(int, s.split(' '))))


class Or(Pattern):
    def __init__(self, a: Refs, b: Refs):
        self.a = a
        self.b = b
    
    def to_regex(self, rules: dict[int, 'Pattern'], depth: int) -> str:
        if depth == Pattern.max_depth:
            return 'x'
        return f'({self.a.to_regex(rules, depth + 1)}|{self.b.to_regex(rules, depth + 1)})'


def part1(inp: list[str]) -> None:
    rules = {}
    it = iter(inp)
    for line in it:
        if line == '':
            break
        if '"' in line:
            rule_id, value = re.fullmatch(r'(\d+): "(\w+)"', line).groups()
            rules[int(rule_id)] = Value(value)
        elif '|' in line:
            rule_id, refs_a, refs_b = re.fullmatch(r'(\d+): ([\d ]+) \| ([\d ]+)', line).groups()
            rules[int(rule_id)] = Or(Refs.parse(refs_a), Refs.parse(refs_b))
        else:
            rule_id, refs = re.fullmatch(r'(\d+): ([\d ]+)', line).groups()
            rules[int(rule_id)] = Refs.parse(refs)

    pattern = rules[0].to_regex(rules, 0)
    count = 0
    for line in it:
        if re.fullmatch(pattern, line):
            count += 1
    print(count)


def part2(inp: list[str]) -> None:
    rules = {}
    it = iter(inp)
    for line in it:
        if line == '8: 42':
            line = '8: 42 | 42 8'
        elif line == '11: 42 31':
            line = '11: 42 31 | 42 11 31'
        
        if line == '':
            break
        if '"' in line:
            rule_id, value = re.fullmatch(r'(\d+): "(\w+)"', line).groups()
            rules[int(rule_id)] = Value(value)
        elif '|' in line:
            rule_id, refs_a, refs_b = re.fullmatch(r'(\d+): ([\d ]+) \| ([\d ]+)', line).groups()
            rules[int(rule_id)] = Or(Refs.parse(refs_a), Refs.parse(refs_b))
        else:
            rule_id, refs = re.fullmatch(r'(\d+): ([\d ]+)', line).groups()
            rules[int(rule_id)] = Refs.parse(refs)
    
    pattern = rules[0].to_regex(rules, 0)
    pattern = re.compile(pattern)
    count = 0
    for line in it:
        if pattern.fullmatch(line):
            count += 1
    print(count)


if __name__ == '__main__':
    part1(TEST)
    part2(TEST1)
    part1(INPUT)
    part2(INPUT)
