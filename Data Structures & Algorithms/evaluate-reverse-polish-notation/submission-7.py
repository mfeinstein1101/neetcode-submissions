class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in ['+', '*', '-', '/']:
                stack.append(int(t))
                continue
            n1 = stack.pop()
            n2 = stack.pop()
            if t == '+':
                stack.append(n1 + n2)
            elif t == '*':
                stack.append(n1*n2)
            elif t == '-':
                stack.append(n2-n1)
            elif t == '/':
                stack.append(int(float(n2)/n1))
        
        return stack[0]