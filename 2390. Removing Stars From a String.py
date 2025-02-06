s = "il**autonrd**cl**nh*up*afpizp****d*a****lst"

class Solution:
    def removeStars(self, s: str) -> str:
        ans=[]
        for i in s:
            if i=='*':
                ans.pop()
            else:
                ans+=[i]
        return "".join(ans)
        
print(Solution().removeStars(s))        