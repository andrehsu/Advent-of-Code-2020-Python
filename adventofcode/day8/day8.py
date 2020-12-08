INPUT = open('input.txt').read().splitlines()
TEST = open('test.txt').read().splitlines()


def run_program(inp: list[str]) -> tuple[int, bool]:
    acc = 0
    seen = set()
    i = 0
    infinite = False
    while True:
        if i == len(inp):
            break
        elif i in seen:
            infinite = True
            break
        else:
            seen.add(i)
        
        op, arg = inp[i].split()
        arg = int(arg)
        if op == 'acc':
            acc += arg
            i += 1
        elif op == 'jmp':
            i += arg
        elif op == 'nop':
            i += 1
        else:
            raise RuntimeError(op, arg)
    
    return acc, infinite


def part1(inp: list[str]) -> None:
    acc, _ = run_program(inp)
    print(acc)


def part2(inp: list[str]) -> None:
    for i in range(len(inp)):
        op, arg = inp[i].split()
        if op == 'jmp':
            copy = inp.copy()
            copy[i] = f'nop {arg}'
        elif op == 'nop':
            copy = inp.copy()
            copy[i] = f'jmp {arg}'
        else:
            continue
        acc, infinite = run_program(copy)
        if not infinite:
            print(f'Change line {i + 1}')
            print(acc)
            return


if __name__ == '__main__':
    print('TESTS:')
    part1(TEST)
    part2(TEST)
    print('SOLUTIONS:')
    part1(INPUT)
    part2(INPUT)
