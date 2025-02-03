ransomNote = "aa"
magazine = "ab"

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i in magazine:
                ransomNote=ransomNote.replace(i,'',1)
                magazine=magazine.replace(i,'',1)
        if ransomNote:
            return False
        return True
    
print(Solution().canConstruct(ransomNote,magazine))