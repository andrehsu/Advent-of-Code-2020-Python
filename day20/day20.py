import operator
import re
from collections import deque
from functools import reduce

import numpy as np

from lib import Image, Tile
from utils import get_variations

INPUT = open('input.txt').read().splitlines()
TEST = open('test.txt').read().splitlines()


def parse_tiles(inp: list[str]) -> list[Tile]:
    it = deque(inp)
    tiles = []
    while it:
        line = it.popleft()
        if line == '':
            continue
        arr = np.zeros((10, 10), dtype=bool)
        id_, = re.fullmatch(r'Tile (\d+):', line).groups()
        id_ = int(id_)
        for i in range(10):
            arr[i] = np.array([i == '#' for i in it.popleft()], dtype=bool)
        tile = Tile(id_, arr)
        tiles.append(tile)
    return tiles


def write_img(combined: np.ndarray, filepath: str):
    with open(filepath, 'w+') as file:
        for i in range(len(combined)):
            for j in range(len(combined[i])):
                c = combined[i, j]
                if c:
                    c = '#'
                else:
                    c = '.'
                file.write(c)
            file.write('\n')


def part1(inp: list[str]) -> None:
    tiles = parse_tiles(inp)
    img = Image()
    img.fit(tiles)
    
    edge_ids = map(lambda tile: tile.id, img.get_edge_tiles())
    print(reduce(operator.mul, edge_ids))


def count_monsters(str_img: list[str]) -> int:
    pattern1 = r'..................#.'
    pattern2 = r'#....##....##....###'
    pattern3 = r'.#..#..#..#..#..#...'
    count = 0
    for i, line in enumerate(str_img):
        for match in re.finditer(pattern2, line):
            start = match.start()
            if re.match(pattern1, str_img[i - 1][start:]) and re.match(pattern3, str_img[i + 1][start:]):
                count += 1
    
    return count


def ndarray_to_list(arr: np.ndarray) -> list[str]:
    l = []
    for i in range(len(arr)):
        sb = []
        for j in range(len(arr[i])):
            b = arr[i, j]
            if b:
                b = '#'
            else:
                b = '.'
            sb.append(b)
        l.append(''.join(sb))
    return l


def part2(inp: list[str]) -> None:
    tiles = parse_tiles(inp)
    img = Image()
    img.fit(tiles)
    
    combined = img.get_combined()
    for i, variation in enumerate(get_variations(combined)):
        write_img(variation, f'solution{i}.txt')
        str_img = ndarray_to_list(variation)
        count = count_monsters(str_img)
        if count > 1:
            total_count = sum(sum(i == '#' for i in line) for line in str_img)
            print(total_count - count * 15)
            return


if __name__ == '__main__':
    part1(TEST)
    part2(TEST)
    part1(INPUT)
    part2(INPUT)
