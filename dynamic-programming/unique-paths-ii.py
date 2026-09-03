class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        min_ways = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]

        for i in range(len(min_ways[0])):
            if obstacleGrid[0][i] == 1:
                break
            else:
                min_ways[0][i] = 1
        for i in range(len(min_ways)):
            if obstacleGrid[i][0] == 1:
                break
            else:
                min_ways[i][0] = 1
        for i in range(1, len(min_ways)):
            for j in range(1, len(min_ways[0])):
                if obstacleGrid[i][j] == 1:
                    min_ways[i][j] == 0
                else:
                    min_ways[i][j] = min_ways[i-1][j] + min_ways[i][j-1]
        print(min_ways)
        return min_ways[-1][-1]

        