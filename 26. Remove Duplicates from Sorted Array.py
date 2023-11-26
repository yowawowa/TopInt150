# https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = list(dict.fromkeys(nums))
        nums.clear()
        for i in res:
            nums.append(i)
        return len(nums)