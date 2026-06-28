from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for word in strs:
            letters = [0] * 26
            for i in range(len(word)):
                letters[ord(word[i]) - ord('a')] += 1
            
            key = tuple(letters)

            if key not in dict:            
                dict[key] = []
        
            dict[key].append(word)

        return list(dict.values())