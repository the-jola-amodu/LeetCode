class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        answer = [0] * n
        stack = []

        for index, num in enumerate(temperatures):
            while stack and stack[-1][0] < num:
                stack_num, stack_pos = stack.pop()
                answer[stack_pos] = index - stack_pos
            stack.append((num, index))
        return answer
        