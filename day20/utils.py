from typing import Iterable, TypeVar

import numpy as np

from direction import Direction

Pair = tuple[int, int]


def get_variations(arr: np.ndarray) -> list[np.ndarray]:
    ret = []
    orig = arr.copy()
    ret.append(arr)
    ret.append(np.rot90(arr))
    ret.append(np.rot90(np.rot90(arr)))
    ret.append(np.rot90(np.rot90(np.rot90(arr))))
    arr = np.flipud(orig)
    ret.append(arr)
    ret.append(np.rot90(arr))
    ret.append(np.rot90(np.rot90(arr)))
    ret.append(np.rot90(np.rot90(np.rot90(arr))))
    arr = np.fliplr(orig)
    ret.append(arr)
    ret.append(np.rot90(np.rot90(arr)))
    
    return ret


def get_pos(pos: Pair, direction: Direction) -> Pair:
    r, c = pos
    d_r, d_c = direction.value
    return r + d_r, c + d_c


T = TypeVar('T')


def get_min_max(*iterables: Iterable[T]) -> tuple[tuple[T, T], ...]:
    ret = []
    for iterable in iterables:
        l = list(iterable)
        ret.append((min(l), max(l)))
    return tuple(ret)
