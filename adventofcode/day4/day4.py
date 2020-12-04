INPUT = open('input.txt').read().splitlines()
import re


def get_passports(input_):
    input_ = input_.copy()
    passports = []
    while input_:
        
        passport = {}
        
        while True:
            if not input_:
                break
            line = input_.pop(0)
            if line == '':
                break
            fields = line.split(' ')
            for field in fields:
                k, v = field.split(':')
                passport[k] = v
        
        passports.append(passport)
    
    return passports


def part1(input_: list[str]):
    passports = get_passports(input_)
    valids = 0
    
    for passport in passports:
        valid = True
        for required in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'):
            if required not in passport:
                valid = False
        
        if valid:
            valids += 1
    
    print(valids)


def part2(input_: list[str]):
    passports = get_passports(input_)
    valids = 0
    for passport in passports:
        valid = True
        for required in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'):
            if required not in passport:
                valid = False
        if not valid:
            continue
        
        byr = int(passport['byr'])
        if not 1920 <= byr <= 2002:
            continue
        iyr = int(passport['iyr'])
        if not 2010 <= iyr <= 2020:
            continue
        eyr = int(passport['eyr'])
        if not 2020 <= eyr <= 2030:
            continue
        if passport['hgt'][-2:] == 'cm':
            hgt = int(passport['hgt'][:-2])
            if not 150 <= hgt <= 193:
                continue
        elif passport['hgt'][-2:] == 'in':
            hgt = int(passport['hgt'][:-2])
            if not 59 <= hgt <= 76:
                continue
        else:
            continue
        hcl = passport['hcl']
        if not re.match(r'^#[\da-f]{6}$', hcl):
            continue
        
        ecl = passport['ecl']
        if ecl not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            continue
        
        pid = passport['pid']
        if not re.match(r'^\d{9}$', pid):
            continue
        
        valids += 1
    print(valids)


if __name__ == '__main__':
    part1(INPUT)
    part2(INPUT)
