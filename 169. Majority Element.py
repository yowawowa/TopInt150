# https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return max(set(nums), key = nums.count)