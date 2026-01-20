class Solution(object):
    def calculate(self, s):
        num_stack = []
        op_stack = []

        i = 0
        n = len(s)

        def precedence(op):
            if op == '+' or op == '-':
                return 1
            if op == '*' or op == '/':
                return 2
            return 0

        def apply_op():
            b = num_stack.pop()
            a = num_stack.pop()
            op = op_stack.pop()

            if op == '+':
                num_stack.append(a + b)
            elif op == '-':
                num_stack.append(a - b)
            elif op == '*':
                num_stack.append(a * b)
            elif op == '/':
                num_stack.append(int(a / b))

        while i < n:
            if s[i] == ' ':
                i += 1
                continue

            if s[i].isdigit():
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                num_stack.append(num)
                continue

            if s[i] in '+-*/':
                while (op_stack and
                       precedence(op_stack[-1]) >= precedence(s[i])):
                    apply_op()
                op_stack.append(s[i])

            i += 1

        while op_stack:
            apply_op()

        return num_stack[0]
