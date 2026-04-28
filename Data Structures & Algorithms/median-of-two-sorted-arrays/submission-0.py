class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        a = len(nums1)
        b = len(nums2)

        l = 0
        r = a

        while l <= r:
            i = (l+r) // 2
            j = (a+b+1) // 2 - i

            a_l = float("-inf") if i == 0 else nums1[i-1]
            a_r = float("inf") if i == a else nums1[i]

            b_l = float("-inf") if j == 0 else nums2[j-1]
            b_r = float("inf") if j == b else nums2[j]

            if a_l <= b_r and b_l <= a_r:
                if (a+b)%2 == 0:
                    return (max(a_l, b_l) + min(a_r, b_r)) / 2
                else:
                    return (max(a_l, b_l))
            elif a_l > b_r:
                r = i - 1
            else:
                l = i + 1