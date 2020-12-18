from abc import ABC, abstractmethod
from typing import Union, Type, Callable

INPUT = open('input.txt').read().splitlines()
TEST = ['((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2']


class Token(ABC):
    def __str__(self):
        return 'token'


class Op(Token, ABC):
    def __str__(self):
        return 'op'


class Add(Op):
    def __str__(self):
        return '+'


class Mult(Op):
    def __str__(self):
        return '*'


class Wrapped(Token):
    def __init__(self, children: list[Token]):
        self.children = children
    
    def __str__(self):
        return '(' + ''.join(map(str, self.children)) + ')'


class Num(Token):
    def __init__(self, value: int):
        self.value = value
    
    def __str__(self):
        return str(self.value)


class Node(ABC):
    @abstractmethod
    def evaluate(self) -> int:
        pass


class Branch(Node):
    def __init__(self, left: 'Node', op: Op, right: 'Node'):
        self.left = left
        self.op = op
        self.right = right
    
    def evaluate(self) -> int:
        if isinstance(self.op, Add):
            return self.left.evaluate() + self.right.evaluate()
        elif isinstance(self.op, Mult):
            return self.left.evaluate() * self.right.evaluate()


class Leaf(Node):
    def __init__(self, value: int):
        self.value = value
    
    def evaluate(self) -> int:
        return self.value


def tokenize(expr: str) -> list[Token]:
    i = 0
    tokens = []
    while i < len(expr):
        c = expr[i]
        if c == ' ':
            i += 1
        elif c == '+':
            tokens.append(Add())
            i += 1
        elif c == '*':
            tokens.append(Mult())
            i += 1
        elif c == '(':
            depth = 0
            close = i + 1
            for j in range(i + 1, len(expr)):
                c_ = expr[j]
                if c_ == '(':
                    depth += 1
                elif c_ == ')':
                    if depth == 0:
                        close = j
                        break
                    else:
                        depth -= 1
            ret = Wrapped(tokenize(expr[i + 1:close]))
            tokens.append(ret)
            i = close + 1
        else:
            try:
                end = expr.index(' ', i + 1)
            except ValueError:
                end = len(expr)
            num = int(expr[i: end])
            tokens.append(Num(num))
            i = end + 1
    
    return tokens


MidType = Union[Node, Token]
NextOp = Callable[[list[MidType]], int]
AstParser = Callable[[list[MidType], NextOp], Node]


def indexOf(midTypes: list[MidType], op: Type[Op]) -> int:
    for i, token in enumerate(midTypes):
        if isinstance(token, op):
            return i
    raise ValueError('op not in midTypes')


def to_node(midType: MidType, ast: AstParser, nextOp: NextOp) -> Node:
    if isinstance(midType, Node):
        return midType
    elif isinstance(midType, Num):
        return Leaf(midType.value)
    elif isinstance(midType, Wrapped):
        return ast(midType.children, nextOp)
    else:
        raise ValueError(midType)


def ast(tokens: list[MidType], next_op: NextOp) -> Node:
    while len(tokens) > 1:
        try:
            i = next_op(tokens)
        except ValueError:
            raise ValueError('Stranded tokens (no more ops)')
        # noinspection PyTypeChecker
        op: Op = tokens[i]
        branch = Branch(to_node(tokens[i - 1], ast, next_op), op, to_node(tokens[i + 1], ast, next_op))
        tokens[i] = branch
        del tokens[i + 1]
        del tokens[i - 1]
    
    return tokens[0]


# def evaluate_part1(expr: str) -> int:
#     """
#     Original part 1 solution
#     :param expr: expression to evaluate
#     :return: result
#     """
#     i = 0
#     total = 0
#     op = '+'
#     while i < len(expr):
#         c = expr[i]
#         num = None
#         if c == ' ':
#             i += 1
#         elif c == '+' or c == '*':
#             op = c
#             i += 1
#         elif c == '(':
#             depth = 0
#             for j in range(i + 1, len(expr)):
#                 c_ = expr[j]
#                 if c_ == '(':
#                     depth += 1
#                 elif c_ == ')':
#                     if depth == 0:
#                         close = j
#                         break
#                     else:
#                         depth -= 1
#             ret = evaluate_part1(expr[i + 1:close])
#             num = ret
#             i = close + 1
#         else:
#             try:
#                 end = expr.index(' ', i + 1)
#             except:
#                 end = len(expr)
#             num = int(expr[i: end])
#             i = end + 1
#
#         if num is not None:
#             if op == '+':
#                 total += num
#             else:
#                 total *= num
#     return total


def part1(inp: list[str]) -> None:
    def next_op(midTypes: list[MidType]) -> int:
        INVALID = len(midTypes) + 1
        try:
            i_add = indexOf(midTypes, Add)
        except ValueError:
            i_add = INVALID
        try:
            i_mult = indexOf(midTypes, Mult)
        except ValueError:
            i_mult = INVALID
        
        if i_add == i_mult == INVALID:
            raise ValueError()
        return min(i_add, i_mult)
    
    print(sum(ast(tokenize(line), next_op).evaluate() for line in inp))


def part2(inp: list[str]) -> None:
    def next_op(midTypes: list[MidType]) -> int:
        try:
            i = indexOf(midTypes, Add)
        except ValueError:
            i = indexOf(midTypes, Mult)
        return i
    
    print(sum(ast(tokenize(line), next_op).evaluate() for line in inp))


if __name__ == '__main__':
    part1(TEST)
    part2(TEST)
    part1(INPUT)
    part2(INPUT)
