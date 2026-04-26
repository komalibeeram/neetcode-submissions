class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        from collections import Counter
        need = Counter(s1)
        win = Counter(s2[:len(s1)])

        if need == win:
            return True
        
        for i in range(len(s1), len(s2)):
            win[s2[i]] += 1
            win[s2[i-len(s1)]] -= 1
            if win[s2[i-len(s1)]] == 0:
                del win[s2[i-len(s1)]]
            
            if win == need:
                return True
        return False
