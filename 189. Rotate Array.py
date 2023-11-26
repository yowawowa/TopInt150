# https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        while k:
            nums.insert(0, (nums.pop()))
            k -= 1
