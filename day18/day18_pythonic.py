INPUT = open('input.txt').read().splitlines()


class NumP1:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return NumP1(self.value + other.value)
    
    def __sub__(self, other):
        return NumP1(self.value * other.value)


class NumP2:
    def __init__(self, value):
        self.value = value
    
    def __truediv__(self, other):
        return NumP2(self.value + other.value)
    
    def __sub__(self, other):
        return NumP2(self.value * other.value)


def convert(expr: str, class_str: str) -> str:
    i = 0
    tokens = []
    while i < len(expr):
        c = expr[i]
        if c == ' ':
            i += 1
        elif c == '+' or c == '*':
            tokens.append(c)
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
            ret = '(' + convert(expr[i + 1:close], class_str) + ')'
            tokens.append(ret)
            i = close + 1
        else:
            try:
                end = expr.index(' ', i + 1)
            except ValueError:
                end = len(expr)
            num = int(expr[i: end])
            tokens.append(f'{class_str}({num})')
            i = end + 1
    
    return ''.join(tokens)


if __name__ == '__main__':
    total_sum = 0
    for line in INPUT:
        expr = convert(line, class_str='NumP1')
        expr = expr.replace('*', '-')
        total_sum += eval(expr, globals()).value
    print(total_sum)
    total_sum = 0
    for line in INPUT:
        expr = convert(line, class_str='NumP2')
        expr = expr.replace('+', '/').replace('*', '-')
        total_sum += eval(expr, globals()).value
    print(total_sum)
