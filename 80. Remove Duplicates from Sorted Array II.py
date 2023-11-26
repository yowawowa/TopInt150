# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in nums:
            while nums.count(i) > 2:
                nums.remove(i)
        return len(nums)