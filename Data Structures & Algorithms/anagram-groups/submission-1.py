class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        d = defaultdict(list)
        for word in strs:
            temp = list(word)
            temp.sort()
            d[tuple(temp)].append(word)
        
        ans = []

        for val in d.values():
            ans.append(val)
        return ans