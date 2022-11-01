class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        
        for i in s:
            if i not in dic:
                dic[i] = 1
                
            else:
                value = dic[i]
                dic[i] = value + 1
        return len({k:v for (k,v) in dic.items() if v > 1}.keys())