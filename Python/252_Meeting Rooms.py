# 252. Meeting Rooms
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort(key = lambda x: x[0])

        for i in range(1,len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True



# 253. Meeting Rooms II
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0

        rooms = []

        intervals.sort(key= lambda x: x[0])

        heapq.heappush(rooms,intervals[0][1])

        for i in intervals[1:]:
            if rooms[0] <= i[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, i[1])

        return len(rooms)
