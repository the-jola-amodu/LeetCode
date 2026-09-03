class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        min_sum = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        prev = 0
        for i in range(len(grid[0])):
            min_sum[0][i] = prev + grid[0][i]
            prev += grid[0][i]
        prev = 0
        for i in range(len(grid)):
            min_sum[i][0] = prev + grid[i][0]
            prev += grid[i][0]

        for i in range(1, len(min_sum)):
            for j in range(1, len(min_sum[0])):
                min_sum[i][j] = grid[i][j] + min(min_sum[i-1][j], min_sum[i][j-1])
        
        print(min_sum)
        return min_sum[-1][-1]