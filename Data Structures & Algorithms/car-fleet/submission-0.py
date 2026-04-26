class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(speed)):
            pairs.append([position[i], speed[i]])
        pairs.sort()

        st = []

        for p, s in pairs[::-1]:
            time = (target - p)/s
            st.append(time)
            if len(st) >=2 and st[-1] <= st[-2]:
                st.pop()
        return len(st)