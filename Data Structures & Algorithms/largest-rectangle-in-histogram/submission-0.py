class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        rse = [-1]*n
        lse = [-1]*n
        st = []

        for i in range(n-1,-1,-1):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            if not st:
                rse[i] = n
            else:
                rse[i] = st[-1]
            st.append(i)
        st = []

        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            if not st:
                lse[i] = -1
            else:
                lse[i] = st[-1]
            st.append(i)
        
        ans = 0
        for i in range(n):
            cur = (rse[i] - lse[i] - 1)*heights[i]
            ans = max(ans, cur)
        return ans