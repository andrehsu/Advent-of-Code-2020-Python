import abc
import re

INPUT = open('input.txt').read().splitlines()
TEST = open('test.txt').read().splitlines()
TEST1 = open('test1.txt').read().splitlines()


class Pattern(abc.ABC):
    @abc.abstractmethod
    def to_regex(self, rules: dict[int, 'Pattern']) -> str:
        pass


class Value(Pattern):
    def __init__(self, value: str):
        self.value = value
    
    def to_regex(self, rules: dict[int, 'Pattern']) -> str:
        return self.value


class Refs(Pattern):
    def __init__(self, ref_ids: list[int]):
        self.ref_ids = ref_ids
    
    def to_regex(self, rules: dict[int, 'Pattern']) -> str:
        sb = []
        for ref_id in self.ref_ids:
            sb.append(rules[ref_id].to_regex(rules))
        return '(' + ''.join(sb) + ')'
    
    @staticmethod
    def parse(s: str) -> 'Refs':
        return Refs(list(map(int, s.split(' '))))


class Or(Pattern):
    def __init__(self, a: Refs, b: Refs):
        self.a = a
        self.b = b
    
    def to_regex(self, rules: dict[int, 'Pattern']) -> str:
        return f'({self.a.to_regex(rules)}|{self.b.to_regex(rules)})'


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
    
    pattern = rules[0].to_regex(rules)
    count = 0
    for line in it:
        if re.fullmatch(pattern, line):
            count += 1
    print(count)


def part2(inp: list[str]) -> None:
    pass


if __name__ == '__main__':
    part1(TEST)
    # part2(TEST)
    part1(INPUT)
    # part2(INPUT)
