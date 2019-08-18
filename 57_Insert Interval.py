# 57. Insert Interval

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]

        # find the correct place to insert the new interval
        i = 0
        while i < len(intervals) and newInterval[0] >= intervals[i][0]:
            i += 1
        intervals.insert(i, newInterval)
        start = i

        # move back 1 place to start merging intervals (skip the previous unnecessary ones)
        if start != 0: start -= 1

        # merging intervals, same as question 56. Merge Intervals
        for i in range(start, len(intervals)-1):
            j = i+1
            while j < len(intervals) and intervals[i][1] >= intervals[j][0]:
                if intervals[i][1] <  intervals[j][1]:
                    intervals[i][1] = intervals[j][1]
                del intervals[j]
        return intervals


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]
        a = -1
        b = -1
        for i in range(len(intervals)):
            if intervals[i][0] <=newInterval[0] <= newInterval[0]:
                a = i
            if i !=0 and intervals[i-1][1] < newInterval[0] < intervals[i][0]:
                a = i
            if intervals[i][0] <= newInterval[1] <= intervals[i][1]:
                b = i
            if i !=0 and intervals[i-1][1] < newInterval[1] < intervals[i][0]:
                b = i-1
            if i == 0 and newInterval[0] < intervals[0][0]:
                a = 0
            if i == len(intervals)-1 and newInterval[1] > intervals[i][1]:
                b = i
        print(a,b)
        if a == -1 and b == -1:
            return intervals.append(newInterval)
        if newInterval[1] < intervals[0][0]:
            res = [newInterval] + intervals
            return res

        if newInterval[0] < intervals[a][0]:
            a1 = newInterval[0]
        else:
            a1 = intervals[a][0]

        if intervals[b][1] < newInterval[1]:
            b1 = newInterval[1]
        else:
            b1 = intervals[b][1]

        res = intervals[:a] + [[a1,b1]] + intervals[b+1:]
        return res
