class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        for i,x in enumerate(zip(*strs)):
            if len(set(x)) > 1:
                return strs[0][:i]
        
        return min(strs)
    
# Time complexity : O(S) , where S is the sum of all characters in all strings.
# Space complexity : O(1). We only used constant extra space.
