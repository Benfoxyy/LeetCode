s = "the sky is   blue   "

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.strip().split()[::-1])
        
print(Solution().reverseWords(s))