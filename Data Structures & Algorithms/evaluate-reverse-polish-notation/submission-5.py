class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in ['+', '*', '-', '/']:
                stack.append(int(tokens[i]))
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                if tokens[i] == '+':
                    stack.append(val2+val1)
                elif tokens[i] == '*':
                    stack.append(val2*val1)
                elif tokens[i] == '-':
                    stack.append(val2-val1)
                else:
                    stack.append(int(val2/val1))

        return stack.pop()