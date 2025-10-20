class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        unravelled = []
        top, left = 0, 0
        bottom, right = len(matrix), len(matrix[0])

        while len(unravelled) < len(matrix) * len(matrix[0]):
            for i in range(left, right):
                unravelled.append(matrix[top][i])
            top += 1

            if not (len(unravelled) < len(matrix) * len(matrix[0])):
                break

            for i in range(top, bottom):
                unravelled.append(matrix[i][right - 1])
            right -= 1

            if not (len(unravelled) < len(matrix) * len(matrix[0])):
                break

            for i in range(right - 1, left - 1, -1):
                unravelled.append(matrix[bottom - 1][i])
            bottom -= 1

            if not (len(unravelled) < len(matrix) * len(matrix[0])):
                break
            
            for i in range(bottom - 1, top - 1, -1):
                unravelled.append(matrix[i][left])
            left += 1
        return unravelled
        