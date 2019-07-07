# 658. Find K Closest Elements

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        index = self.findIndex(arr, x)
        l, r = index, index

        while r - l < k:
            if l == 0: return arr[:k]
            if r == len(arr): return arr[-k:]
            if x - arr[l-1] <= arr[r] - x:
                l -= 1
            else:
                r += 1
        return arr[l:r]


    def findIndex(self, arr, target):
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = l + (r-l)//2
            if arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l
