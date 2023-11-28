class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def forward_notation(self):
        print(self.value, end=" ")
        if self.left is not None:
            self.left.forward_notation()
        if self.right is not None:
            self.right.forward_notation()

    def backward_notation(self):
        if self.left is not None:
            self.left.backward_notation()
        if self.right is not None:
            self.right.backward_notation()
        print(self.value, end=" ")

    def evaluate_forward_steps(self):
        if self.left is not None:
            self.left.evaluate_forward_steps()
        if self.right is not None:
            self.right.evaluate_forward_steps()
        print(f"\nКрок: {self.value} {self.left.value if self.left else ''} {self.right.value if self.right else ''}")
        print(f"Результат: {self.evaluate()}")

    def evaluate_backward_steps(self):
        if self.left is not None:
            self.left.evaluate_backward_steps()
        if self.right is not None:
            self.right.evaluate_backward_steps()
        print(f"\nКрок: {self.value} {self.left.value if self.left else ''} {self.right.value if self.right else ''}")
        print(f"Результат: {self.evaluate()}")

    def evaluate(self):
        if isinstance(self.value, (int, float)):
            return float(self.value)
        elif self.value.isalpha():
            pass
        else:
            left_result = self.left.evaluate() if self.left else 0
            right_result = self.right.evaluate() if self.right else 0
            if self.value == '+':
                return left_result + right_result
            elif self.value == '-':
                return left_result - right_result
            elif self.value == '*':
                return left_result * right_result
            elif self.value == '/':
                return left_result / right_result
            elif self.value == '^':
                return left_result ** right_result
            else:
                raise ValueError(f"Invalid operator: {self.value}")

def build_tree(expression):
    operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def is_operator(token):
        return token in operators

    def higher_precedence(op1, op2):
        return operators[op1] >= operators[op2]

    def pop_operators(operators_stack, values_stack, current_precedence):
        while (operators_stack and
               operators_stack[-1] != '(' and
               is_operator(operators_stack[-1]) and
               higher_precedence(operators_stack[-1], current_precedence)):
            operator = operators_stack.pop()
            right = values_stack.pop()
            left = values_stack.pop()
            node = Tree(operator)
            node.left = left
            node.right = right
            values_stack.append(node)

    tokens = expression.replace(' ', '')
    values_stack = []
    operators_stack = []

    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token.isdigit():
            j = i
            while j < len(tokens) and (tokens[j].isdigit() or tokens[j] == '.'):
                j += 1
            values_stack.append(Tree(float(tokens[i:j])))
            i = j
        elif token.isalpha():
            j = i
            while j < len(tokens) and (tokens[j].isalpha() or tokens[j].isdigit()):
                j += 1
            values_stack.append(Tree(tokens[i:j]))
            i = j
        elif is_operator(token):
            pop_operators(operators_stack, values_stack, token)
            operators_stack.append(token)
            i += 1
        elif token == '(':
            operators_stack.append(token)
            i += 1
        elif token == ')':
            pop_operators(operators_stack, values_stack, '+')
            operators_stack.pop()
            i += 1
        else:
            raise ValueError(f"Invalid token: {token}")

    pop_operators(operators_stack, values_stack, '+')

    return values_stack[0]

def print_tree(root, level=0, prefix="Корінь: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.value))
        if root.left is not None or root.right is not None:
            print_tree(root.left, level + 1, "Л--> ")
            print_tree(root.right, level + 1, "П--> ")

expression = "5^2 + 8 / 2 * (7-4)"
root = build_tree(expression)
print_tree(root)

print("\nПрямий польський запис:")
root.forward_notation()

print("\nЗворотній польський запис:")
root.backward_notation()

print("\nКроки для обчислення прямого польського запису:")
root.evaluate_forward_steps()

print("\nКроки для обчислення зворотнього польського запису:")
root.evaluate_backward_steps()
