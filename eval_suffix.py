import operator


class Stack:
    """栈（FILO）"""

    def __init__(self):
        self.elems = []

    def push(self, elem):
        """入栈"""
        self.elems.append(elem)

    def pop(self):
        """出栈"""
        return self.elems.pop()

    @property
    def is_empty(self):
        """检查栈是否为空"""
        return len(self.elems) == 0


def eval_suffix(expr):
    """逆波兰表达式求值"""
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    stack = Stack()
    for item in expr.split():
        if item.isdigit():
            stack.push(float(item))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            stack.push(operators[item](num1, num2))

    return stack.pop()


if __name__ == '__main__':
    print(eval_suffix('5 2 3 + *'))
