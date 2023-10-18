# 215. Kth Largest Element in an Array

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap,nums[i])
        for i in range(len(nums)-k):
            heapq.heappop(heap)
        return heapq.heappop(heap)
