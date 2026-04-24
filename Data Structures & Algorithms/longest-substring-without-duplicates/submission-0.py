class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        seen = set()
        l = 0

        for r in range(len(s)):
            ch = s[r]
            while ch in seen:
                seen.remove(s[l])
                l += 1
            ans = max(ans, r-l+1)
            seen.add(ch)
        return ans
