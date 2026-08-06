class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] < result[-1][0] and result[-1][0]<= intervals[i][1] <= result[-1][1]:
                result[-1][0] = intervals[i][0]
            elif intervals[i][0] < result[-1][0] and intervals[i][1] > result[-1][1]:
                result[-1][0] = intervals[i][0]
                result[-1][1] = intervals[i][1]
            elif intervals[i][0] <= result[-1][1] and intervals[i][1] >= result[-1][1]:
                result[-1][1] = intervals[i][1]
            elif intervals[i][0] >= result[-1][0] and intervals[i][1] <= result[-1][1]:
                continue
            else:
                result.append(intervals[i])
        return result
        