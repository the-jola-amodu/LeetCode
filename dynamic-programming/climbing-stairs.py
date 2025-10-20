class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        memo = [0] * n
        memo[0] = 1
        memo[1] = 2
        for i in range(2, n):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[n-1]
        