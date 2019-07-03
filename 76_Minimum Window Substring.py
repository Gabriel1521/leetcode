# 76. Minimum Window Substring

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        target_count_dict = collections.defaultdict(int)
        for ch in t:
            target_count_dict[ch] += 1
        remain_missing = len(t)
        start_pos, end_pos = 0, float('inf')
        current_start = 0

        for current_end, ch in enumerate(s, 1):
            if target_count_dict[ch] > 0:
                remain_missing -= 1
            target_count_dict[ch] -= 1

            if remain_missing == 0:
                while target_count_dict[s[current_start]] < 0:
                    target_count_dict[s[current_start]] += 1
                    current_start += 1
                if current_end - current_start < end_pos - start_pos:
                    start_pos, end_pos = current_start, current_end

                target_count_dict[s[current_start]] += 1
                remain_missing += 1
                current_start += 1

        return s[start_pos:end_pos] if end_pos != float('inf') else ""


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]
