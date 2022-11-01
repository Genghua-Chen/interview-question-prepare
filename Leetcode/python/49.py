class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        h = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in h:
                h[sortedWord] = [word]
            else:
                h[sortedWord].append(word)

        return [value for value in h.values()]
    
        