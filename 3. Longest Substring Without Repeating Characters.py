s = "pwwkew"

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = ''
        for i in s:
            if i not in x:
                x += i
            else:
                if i != x[0]:
                    x = x[1:]
        return len(x)
    

print(Solution().lengthOfLongestSubstring(s))