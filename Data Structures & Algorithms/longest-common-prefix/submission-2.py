class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first=strs[0]
        lenFirst=len(first)
        for i in range(lenFirst):
            prefix=first[:i+1]
            for word in strs[1:]:
                if not word.startswith(prefix):
                    return first[:i]  
        return first        