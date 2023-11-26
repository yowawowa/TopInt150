# https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
            while nums.count(val) != 0:
                nums.remove(val)