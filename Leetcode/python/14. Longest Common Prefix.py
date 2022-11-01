class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first=strs[0]
        
        for i, c in enumerate(first):

            for string in strs:
                if len(string) == i or string[i] != c:
                    return first[:i]

        return first