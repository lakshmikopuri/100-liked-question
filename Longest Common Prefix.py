#Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
           return ""
        strs.sort()
        prefix=""
        for i in range(len(strs[0])):
            if strs[0][i]==strs[-1][i]:
                prefix=prefix+strs[0][i]
                i=i+1
            else:
                break
        return prefix
