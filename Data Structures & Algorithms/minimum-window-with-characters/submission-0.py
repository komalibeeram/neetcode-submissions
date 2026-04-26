class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        d = Counter(t)
        req = len(d)
        found = 0

        win = {}
        ans = float("inf"), None, None
        l = 0
        r = 0
        while r < len(s):
            ch = s[r]
            win[ch] = win.get(ch, 0)+1
            if ch in d and win[ch] == d[ch]:
                found += 1
            while found == req and l <= r:
                w = r - l + 1
                if w < ans[0]:
                    ans = (w, l, r)
                ch = s[l]
                win[ch] -= 1
                if ch in d and win[ch] < d[ch]:
                    found -= 1
                l += 1
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2]+1]