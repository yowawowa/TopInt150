# https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
            res[len(nums) - i - 1] *= postfix
            postfix *= nums[len(nums) - i - 1]
        return res