class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        
        s=s.lower()
        ans = ""
        for ch in s:
            if ch.isalnum():
                ans += ch
        print(ans)
        r = len(ans) - 1
        while l < r:
            if ans[l] != ans[r]:
                return False
            l+=1
            r-=1
        return True