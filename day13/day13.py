import os
import re
from operator import itemgetter

import requests
from dotenv import load_dotenv

load_dotenv('../.env')

INPUT = open('input.txt').read().splitlines()
TEST = open('TEST.txt').read().splitlines()

APP_ID = os.getenv('APP_ID')
if APP_ID is None:
    raise EnvironmentError('APP_ID missing')


def part1(inp: list[str]) -> None:
    earliest = int(inp[0])
    buses = [int(i) for i in inp[1].split(',') if i != 'x']
    deltas = []
    for bus in buses:
        departs = (earliest // bus + 1) * bus
        deltas.append((bus, departs - earliest))
    
    soonest = min(deltas, key=itemgetter(1))
    print(soonest[0] * soonest[1])


def part2(inp: list[str]) -> None:
    buses = inp[1].split(',')
    equations = []
    for i, bus in enumerate(buses):
        if bus == 'x':
            continue
        equations.append(f'(t+{i}) mod {bus} = 0')
    equations_system = ','.join(equations)
    payload = {
        'appid': APP_ID,
        'output': 'json',
        'input': equations_system
    }
    base_url = 'http://api.wolframalpha.com/v2/query'
    res = requests.get(base_url, params=payload)
    json = res.json()
    pods = json['queryresult']['pods']
    for pod in pods:
        if pod['title'] == 'Integer solution':
            subpod = pod['subpods'][0]
            solution = subpod['plaintext']
            answer = re.match(r't = \d+ n \+ (\d+), n element Z', solution).group(1)
            print(answer)
            return


if __name__ == '__main__':
    print('Test:')
    part1(TEST)
    part2(TEST)
    print('Solution:')
    part1(INPUT)
    part2(INPUT)
