class Solution(object):
    def calPoints(self, operations):
        result = []
        for operation in operations:
            if operation == "C":
                result.pop()
            elif operation == "D":
                result.append(result[-1] * 2)
            elif operation == "+":
                result.append(result[-1] + result[-2])
            else:
                result.append(int(operation))
        return sum(result)
        