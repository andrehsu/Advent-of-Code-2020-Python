INPUT = open('input.txt').read().splitlines()


def part1(input_: list[str]) -> None:
    count = 0
    for row in input_:
        range_, letter, password = row.split()
        fr, to = range_.split('-')
        fr = int(fr)
        to = int(to)
        letter = letter[0]
        if fr <= password.count(letter) <= to:
            count += 1
    
    print(count)


def part2(input_: list[str]) -> None:
    count = 0
    for row in input_:
        range_, letter, password = row.split()
        fr, to = range_.split('-')
        fr = int(fr)
        to = int(to)
        letter = letter[0]
        a = password[fr - 1] == letter
        b = password[to - 1] == letter
        if a != b:
            count += 1
    
    print(count)


if __name__ == '__main__':
    part1(INPUT)
    part2(INPUT)
