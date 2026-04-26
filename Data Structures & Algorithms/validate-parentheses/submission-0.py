class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        d = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        for ch in s:
            if ch in d:
                if st and st[-1] == d[ch]:
                    st.pop()
                else:
                    return False
            else:
                st.append(ch)
        return True if not st else False