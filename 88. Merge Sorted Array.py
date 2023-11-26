#https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while n > 0:
            nums1.pop()
            n -= 1
        for i in nums2:
            nums1.append(i)
        nums1.sort()
