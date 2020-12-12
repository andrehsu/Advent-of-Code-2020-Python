INPUT = open('input.txt').read().splitlines()
TEST = open('test.txt').read().splitlines()

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


def part1(inp: list[str]) -> None:
    x = y = 0
    d = EAST
    
    def move(d_=None):
        nonlocal x, y
        if d_ is None:
            d_ = d
        if d_ == NORTH:
            y += value
        elif d_ == SOUTH:
            y -= value
        elif d_ == EAST:
            x += value
        elif d_ == WEST:
            x -= value
        else:
            raise ValueError(d_)
    
    def left():
        nonlocal d
        d -= value // 90
        if d < 0:
            d += 4
    
    def right():
        nonlocal d
        d += value // 90
        if d > 3:
            d -= 4
    
    for line in inp:
        action = line[0]
        value = int(line[1:])
        if action == 'N':
            move(NORTH)
        elif action == 'S':
            move(SOUTH)
        elif action == 'E':
            move(EAST)
        elif action == 'W':
            move(WEST)
        elif action == 'L':
            left()
        elif action == 'R':
            right()
        elif action == 'F':
            move()
        else:
            raise ValueError(action)
    
    print(abs(x) + abs(y))


def part2(inp: list[str]) -> None:
    waypoint_x = 10
    waypoint_y = 1
    x = y = 0
    
    def move(d):
        nonlocal waypoint_x, waypoint_y
        if d == NORTH:
            waypoint_y += value
        elif d == SOUTH:
            waypoint_y -= value
        elif d == EAST:
            waypoint_x += value
        elif d == WEST:
            waypoint_x -= value
        else:
            raise ValueError(d)
    
    def rotate():
        nonlocal waypoint_x, waypoint_y
        v = (value + 360) % 360
        if v == 270:
            waypoint_x, waypoint_y = waypoint_y, - waypoint_x
        elif v == 180:
            waypoint_x, waypoint_y = -waypoint_x, -waypoint_y
        elif v == 90:
            waypoint_x, waypoint_y = -waypoint_y, waypoint_x
    
    def forward():
        nonlocal x, y
        x += waypoint_x * value
        y += waypoint_y * value
    
    for line in inp:
        action = line[0]
        value = int(line[1:])
        if action == 'N':
            move(NORTH)
        elif action == 'S':
            move(SOUTH)
        elif action == 'E':
            move(EAST)
        elif action == 'W':
            move(WEST)
        elif action == 'L':
            rotate()
        elif action == 'R':
            value = -value
            rotate()
        elif action == 'F':
            forward()
        else:
            raise ValueError(action)
    
    print(abs(x) + abs(y))


if __name__ == '__main__':
    print('Test:')
    part1(TEST)
    part2(TEST)
    print('Solution:')
    part1(INPUT)
    part2(INPUT)
