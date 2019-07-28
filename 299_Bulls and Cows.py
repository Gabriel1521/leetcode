# 299. Bulls and Cows

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        l1, l2 = [0]*10, [0]*10
        nums1, nums2 = map(int, secret), map(int, guess)
        length = len(secret)
        for i in xrange(length):
            if nums1[i] == nums2[i]:
                bulls += 1
            else:
                l1[nums1[i]] += 1
                l2[nums2[i]] += 1
        cows = sum(map(min, zip(l1,l2)))
        return '%dA%dB' % (bulls, cows)
