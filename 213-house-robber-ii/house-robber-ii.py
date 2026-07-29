class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def helper(houses: List[int]) -> int:
            prev1, prev2 = 0,0
            for num in houses:
                temp = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = temp
            return prev1
        return max(helper(nums[:-1]), helper(nums[1:]))
