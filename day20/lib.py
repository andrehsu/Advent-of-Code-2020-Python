from collections import defaultdict
from dataclasses import dataclass
from typing import Union

import numpy as np

from direction import Direction
from utils import Pair, get_pos, get_min_max, get_variations


class Image:
    def __init__(self):
        self.arr: dict[Pair, 'Tile'] = {}
    
    def get_free_spaces(self) -> set[Pair]:
        ret = set()
        for pos in self.arr:
            for direction in Direction:
                new_pos = get_pos(pos, direction)
                if new_pos not in self.arr:
                    ret.add(new_pos)
        
        return ret
    
    def get_combined(self) -> np.ndarray:
        rows = list(map(lambda p: p[0], self.arr.keys()))
        cols = list(map(lambda p: p[1], self.arr.keys()))
        
        min_r = min(rows)
        max_r = max(rows)
        min_c = min(cols)
        max_c = max(cols)
        output = defaultdict(bool)
        for r in range(min_r, max_r + 1):
            for c in range(min_c, max_c + 1):
                tile = self.arr[(r, c)].trimmed()
                for r_ in range(8):
                    for c_ in range(8):
                        output[(r * 8 + r_, c * 8 + c_)] = tile.arr[r_, c_]
        
        rows, cols = zip(*output.keys())
        
        min_r = min(rows)
        max_r = max(rows)
        min_c = min(cols)
        max_c = max(cols)
        
        combined = []
        for r in range(min_r, max_r + 1):
            row = []
            for c in range(min_c, max_c + 1):
                row.append(output[(r, c)])
            combined.append(row)
        
        return np.array(combined, dtype=bool)
    
    def tile_fits(self, pos: Pair, tile: 'Tile') -> bool:
        for direction in Direction:
            new_pos = get_pos(pos, direction)
            if new_pos not in self.arr:
                continue
            if not tile.match(self.arr[new_pos], direction):
                return False
        
        return True
    
    def find_fitting_tile(self, free_space: Pair, tiles: list['Tile']) -> Union['Tile', None]:
        for tile in tiles:
            for variation in tile.variations():
                if self.tile_fits(free_space, variation):
                    return variation
        return
    
    def fit(self, tiles: list['Tile']) -> None:
        tiles = tiles.copy()
        self.arr = {(0, 0): tiles.pop()}
        while tiles:
            free_spaces = self.get_free_spaces()
            for free_space in free_spaces:
                tile = self.find_fitting_tile(free_space, tiles)
                if tile is not None:
                    tiles.remove(tile)
                    self.arr[free_space] = tile
    
    def get_edge_tiles(self) -> list['Tile']:
        ret = []
        rows, cols = get_min_max(*zip(*self.arr.keys()))
        for r in rows:
            for c in cols:
                ret.append(self.arr[r, c])
        return ret


@dataclass(frozen=True)
class Tile:
    id: int
    arr: np.ndarray
    
    def variations(self) -> list['Tile']:
        ret = []
        for arr in get_variations(self.arr):
            ret.append(Tile(self.id, arr))
        
        return ret
    
    def match(self, other: 'Tile', direction: Direction) -> bool:
        if direction == Direction.TOP:
            return np.array_equal(self.arr[0, :], other.arr[-1, :])
        elif direction == Direction.DOWN:
            return np.array_equal(self.arr[-1, :], other.arr[0, :])
        elif direction == Direction.LEFT:
            return np.array_equal(self.arr[:, 0], other.arr[:, -1])
        elif direction == Direction.RIGHT:
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
    
    def trimmed(self) -> 'Tile':
        trimmed_arr = self.arr[1:-1, 1:-1]
        return Tile(self.id, trimmed_arr)
