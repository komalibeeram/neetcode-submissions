class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        import heapq
        from collections import Counter
        d = Counter(nums)
        heap = [(-freq, num) for (num, freq) in d.items()]

        heapq.heapify(heap)
        ans = []

        while k:
            freq, num = heapq.heappop(heap)
            ans.append(num)
            k -= 1
        return ans