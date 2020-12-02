input_ = open('input.txt').read().splitlines()


def part1(inp: list[str]) -> None:
    count = 0
    for row in inp:
        rang, letter, password = row.split()
        fr, to = rang.split('-')
        fr = int(fr)
        to = int(to)
        letter = letter[0]
        co = 0
        for i in password:
            if i == letter:
                co += 1
        
        if fr <= co <= to:
            count += 1
    
    print(count)


def part2(inp: list[str]) -> None:
    count = 0
    for row in inp:
        rang, letter, password = row.split()
        fr, to = rang.split('-')
        fr = int(fr)
        to = int(to)
        letter = letter[0]
        a = password[fr - 1] == letter
        b = password[to - 1] == letter
        if a != b:
            count += 1
    
    print(count)


if __name__ == '__main__':
    part1(input_)
    part2(input_)
