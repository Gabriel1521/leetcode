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


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for x in nums[k:]:
            if x > heap[0]:
                heapq.heapreplace(heap, x)
        return heap[0]        