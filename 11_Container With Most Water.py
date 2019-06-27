# 11. Container With Most Water

class Solution(object):
    def maxArea(self, height):
        L, R, width, res = 0, len(height)-1, len(height)-1, 0

        while width > 0:
            if height[L] <= height[R]:
                res = max(res, height[L]*width)
                L = L + 1
                width = width - 1
            else:
                res = max(res, height[R]*width)
                R = R - 1
                width = width - 1

        return res


# 42. Trapping Rain Water

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lr, left, right, water = [], 0, 0, 0
        for i in range(len(height)-1,-1,-1):
          right = max(right,height[i])
          lr.append(right)
        lr.reverse()
        for i in range(len(height)):
          left = max(left, height[i])
          water += min(left,lr[i]) - height[i]

        return water
