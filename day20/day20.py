import operator
import re
from collections import deque
from functools import reduce

import numpy as np

from lib import Image, Tile, get_variations, count_monsters

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


def part1(inp: list[str]) -> None:
    tiles = parse_tiles(inp)
    img = Image()
    img.fit(tiles)
    
    edge_ids = map(lambda tile: tile.id, img.get_edge_tiles())
    print(reduce(operator.mul, edge_ids))


def part2(inp: list[str]) -> None:
    tiles = parse_tiles(inp)
    img = Image()
    img.fit(tiles)
    
    combined = img.get_combined()
    for i, variation in enumerate(get_variations(combined)):
        monster_count = count_monsters(variation)
        if monster_count > 1:
            total_count = sum(sum(row) for row in variation)
            print(total_count - monster_count * 15)
            return


if __name__ == '__main__':
    part1(TEST)
    part2(TEST)
    part1(INPUT)
    part2(INPUT)
