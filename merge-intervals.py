class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        #intervals = [[1,3],[2,6],[8,10],[15,18]]
        #intervals = [[1,4],[0,4]]
        intervals.sort(key = lambda i : i[0])
        sol = []
        sol.append(intervals[0])
        for i, interval in enumerate(intervals):
            if i == 0:
                continue
            if interval[0] <= sol[-1][1]:
                lastElement = max(sol[-1][1], interval[1])
                newInterval = [sol[-1][0], lastElement]
                sol[-1] = newInterval
            else:
                sol.append(interval)
        print(sol)
        return sol

sol = Solution()
intervals = [[1,4],[4,5]]
sol.merge(intervals)
