class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = self.search(nums, target)
        h = self.search(nums, target+1)-1

        if l<= h: return [l,h]

        return [-1,-1]

    def search(self, nums, x):
        l = 0
        h = len(nums)

        while l < h:
            mid = (l+h)//2
            if nums[mid]< x:
                l = mid+1
            else:
                h = mid
        return l