class Solution(object):
    def searchMatrix(self, matrix, target):
        left = 0
        right = len(matrix) - 1
        while left <= right:
            middle = (left + right) // 2
            inner_left = 0
            inner_right = len(matrix[middle]) - 1
            while inner_left <= inner_right:
                inner_middle = (inner_left + inner_right) // 2
                if matrix[middle][inner_middle] == target:
                    return True
                elif target > matrix[middle][inner_middle]:
                    inner_left = inner_middle + 1
                else:
                    inner_right = inner_middle - 1
            if target > matrix[middle][-1]:
                left = middle + 1
            elif target < matrix[middle][0]:
                right = middle - 1
            else:
                return False
        return False