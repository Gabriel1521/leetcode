# 4	Median of Two Sorted Arrays

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        n = len1 + len2
        if n%2 == 0:
            return (self.findkth(nums1, 0, len1, nums2, 0, len2, n/2)+self.findkth(nums1, 0, len1, nums2, 0, len2, n/2+1))/2.0
        else:
            return self.findkth(nums1, 0, len1, nums2, 0, len2, n/2+1)

    def findkth(self,nums1, start1, len1, nums2, start2, len2, k):
        if len1-start1 > len2-start2:
            return self.findkth(nums2, start2, len2, nums1, start1,len1, k)
        if len1-start1==0:
            return nums2[k-1]
        if k== 1:
            return min(nums1[start1],nums2[start2])
        p1 = start1 + min(len1-start1,k/2)
        p2 = start2 + k - p1 + start1
        if nums1[p1-1] < nums2[p2-1]:
            return self.findkth(nums1,p1,len1,nums2,start2,len2,k-p1+start1)
        elif nums1[p1-1] > nums2[p2-1]:
            return self.findkth(nums1,start1,len1,nums2,p2,len2,k-p2+start2)
        else:
            return nums1[p1-1]
