from collections import defaultdict

INPUT = '6,13,1,15,2,0'
TEST = '0,3,6'


def part1(inp: str) -> None:
    nums = list(map(int, inp.split(',')))
    history = defaultdict(list)
    i = 1
    spoken = -1
    for num in nums:
        history[num].append(i)
        spoken = num
        i += 1
    while True:
        if len(history[spoken]) == 1:
            spoken = 0
            history[spoken].append(i)
        else:
            last, lastlast, *_ = history[spoken][::-1]
            spoken = last - lastlast
            history[spoken].append(i)
        
        if i == 2020:
            print(spoken)
            return
        i += 1


class LastTwo:
    def __init__(self):
        self.first = -1
        self.second = -1
    
    @property
    def has_two(self):
        return self.first != -1
    
    def add(self, x):
        self.first = self.second
        self.second = x
    
    @property
    def diff(self):
        return self.second - self.first
    
    def __str__(self):
        return f'{self.first} {self.second}'


def part2(inp: str) -> None:
    nums = list(map(int, inp.split(',')))
    history = defaultdict(lambda: LastTwo())
    i = 1
    spoken = -1
    for num in nums:
        history[num].add(i)
        spoken = num
        i += 1
    while True:
        if not history[spoken].has_two:
            spoken = 0
            history[spoken].add(i)
        else:
            spoken = history[spoken].diff
            history[spoken].add(i)
        
        if i == 30000000:
            print(spoken)
            return
        i += 1


if __name__ == '__main__':
    part1(TEST)
    part2(TEST)
    part1(INPUT)
    part2(INPUT)
