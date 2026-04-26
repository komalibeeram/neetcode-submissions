class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)

        st = []
        for i in range(len(temperatures)):
            while st and st[-1][0] < temperatures[i]:
                temp, ind = st.pop()
                ans[ind] = i-ind
            st.append([temperatures[i], i])
        return ans
