import math

class Solution(object):
    def evalRPN(self, tokens):
        calc = []
        for i in range(len(tokens)):
            if tokens[i] == '+':
                result = calc[-2] + calc[-1]
                calc.pop()
                calc.pop()
                calc.append(int(result))
            elif tokens[i] == '-':
                result = calc[-2] - calc[-1]
                calc.pop()
                calc.pop()
                calc.append(int(result))
            elif tokens[i] == '*':
                result = calc[-2] * calc[-1]
                calc.pop()
                calc.pop()
                calc.append(int(result))
            elif tokens[i] == '/':
                result = calc[-2] / calc[-1]
                result = math.trunc(result)
                print(result)
                calc.pop()
                calc.pop()
                calc.append(result)
            else:
                calc.append(int(tokens[i]))
        return calc[-1]
        