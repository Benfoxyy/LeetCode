s = "IceCreAm"

class Solution:
    def reverseVowels(self, s: str) -> str:
        t = []
        for i in s:
            if i in 'aAeEiIoOuU':
                s = s.replace(i,'*',1)
                t.append(i)
        for j in s:
            if j == '*':
                s = s.replace(j,t.pop(),1)
        return s
            
                
print(Solution().reverseVowels(s))