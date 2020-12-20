import re
from collections import deque, defaultdict

import numpy as np

INPUT = open('input.txt').read().splitlines()
TEST = open('test.txt').read().splitlines()

Pair = tuple[int, int]

TOP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
directions = (TOP, DOWN, LEFT, RIGHT)


class Tile:
    def __init__(self, id: int, arr: np.ndarray):
        self.id = id
        self.arr = arr
    
    def variations(self) -> list['Tile']:
        ret = []
        for arr in [self.arr, np.flipud(self.arr), np.fliplr(self.arr)]:
            ret.append(Tile(self.id, arr))
            ret.append(Tile(self.id, np.rot90(arr)))
            ret.append(Tile(self.id, np.rot90(np.rot90(arr))))
            ret.append(Tile(self.id, np.rot90(np.rot90(np.rot90(arr)))))
        
        return ret
    
    def match(self, other: 'Tile', direction: Pair) -> bool:
        if direction == TOP:
            return np.array_equal(self.arr[0, :], other.arr[-1, :])
        elif direction == DOWN:
            return np.array_equal(self.arr[-1, :], other.arr[0, :])
        elif direction == LEFT:
            return np.array_equal(self.arr[:, 0], other.arr[:, -1])
        elif direction == RIGHT:
            return np.array_equal(self.arr[:, -1], other.arr[:, 0])
        else:
            raise ValueError(direction)
    
    def __hash__(self):
        return hash(self.id)
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Tile):
            return False
        return self.id == other.id
    
    def __str__(self) -> str:
        sb = []
        for r in range(10):
            for c in range(10):
                c = self.arr[r, c]
                if c:
                    c = '#'
                else:
                    c = '.'
                sb.append(c)
            sb.append('\n')
        return ''.join(sb)
    
    def trim(self) -> None:
        self.arr = self.arr[1:-1, 1:-1]


def get_free_spaces(img: dict[Pair, Tile]) -> list[Pair]:
    ret = []
    for pos in img:
        for direction in directions:
            new_pos = get_pos(pos, direction)
            if new_pos not in img:
                ret.append(new_pos)
    
    return ret


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


def get_pos(pos: Pair, direction: Pair) -> Pair:
    r, c = pos
    d_r, d_c = direction
    return r + d_r, c + d_c


def print_img(img: dict[Pair, Tile]):
    rows = list(map(lambda p: p[0], img.keys()))
    cols = list(map(lambda p: p[1], img.keys()))
    
    min_r = min(rows)
    max_r = max(rows)
    min_c = min(cols)
    max_c = max(cols)
    output = defaultdict(lambda: '.')
    for r in range(min_r, max_r + 1):
        for c in range(min_c, max_c + 1):
            if (r, c) not in img:
                continue
            tile = img[(r, c)]
            for r_ in range(8):
                for c_ in range(8):
                    output[(r * 8 + r_, c * 8 + c_)] = tile.arr[r_, c_]
    
    rows, cols = list(zip(*output.keys()))
    
    min_r = min(rows)
    max_r = max(rows)
    min_c = min(cols)
    max_c = max(cols)
    
    with open('output.txt', 'w+') as file:
        for r in range(min_r, max_r + 1):
            for c in range(min_c, max_c + 1):
                char = output[(r, c)]
                if char:
                    char = '#'
                else:
                    char = '.'
                file.write(char)
            file.write('\n')


def part1(inp: list[str]) -> None:
    tiles = parse_tiles(inp)
    
    def fits(pos: Pair, tile: Tile) -> bool:
        for direction in directions:
            new_pos = get_pos(pos, direction)
            if new_pos not in img:
                continue
            if not tile.match(img[new_pos], direction):
                return False
        
        return True
    
    def try_free_space():
        for tile in tiles:
            for variation in tile.variations():
                if fits(free_space, variation):
                    img[free_space] = variation
                    tiles.remove(tile)
                    return True
        return False
    
    img: dict[Pair, Tile] = {(0, 0): tiles.pop()}
    while tiles:
        free_spaces = get_free_spaces(img)
        for free_space in free_spaces:
            if try_free_space():
                break
    rows, cols = list(zip(*img.keys()))
    
    min_r = min(rows)
    max_r = max(rows)
    min_c = min(cols)
    max_c = max(cols)
    total = 1
    for r in [min_r, max_r]:
        for c in [min_c, max_c]:
            total *= img[(r, c)].id
    print(total)


def part2(inp: list[str]) -> None:
    tiles = parse_tiles(inp)
    
    def fits(pos: Pair, tile: Tile) -> bool:
        for direction in directions:
            new_pos = get_pos(pos, direction)
            if new_pos not in img:
                continue
            if not tile.match(img[new_pos], direction):
                return False
        
        return True
    
    def try_free_space():
        for tile in tiles:
            for variation in tile.variations():
                if fits(free_space, variation):
                    img[free_space] = variation
                    tiles.remove(tile)
                    return True
        return False
    
    img: dict[Pair, Tile] = {(0, 0): tiles.pop()}
    while tiles:
        free_spaces = get_free_spaces(img)
        for free_space in free_spaces:
            if try_free_space():
                break
    
    for k, tile in img.items():
        tile.trim()
    
    print_img(img)


if __name__ == '__main__':
    part1(TEST)
    part2(TEST)
    # part1(INPUT)
    # part2(INPUT)
