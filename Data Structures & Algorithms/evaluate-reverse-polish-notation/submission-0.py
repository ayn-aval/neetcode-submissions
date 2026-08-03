class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+': lambda a,b : a+b,
                     '-': lambda a,b : a-b,
                     '*': lambda a,b : a*b,
                     '/': lambda a,b : int(a/b)}
        for t in tokens:
            if t in operators:
                a = stack.pop()
                b = stack.pop()
                res = operators[t](b,a)
                stack.append(res)
            else:
                stack.append(int(t))
        return stack[-1]