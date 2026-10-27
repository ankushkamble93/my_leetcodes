from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        # Prefix sum frequency map initialized with 0 sum occurring once
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1

        for num in nums:
            current_sum += num
            # If (current_sum - k) exists, it means we found a subarray that sums to k
            if (current_sum - k) in prefix_sums:
                count += prefix_sums[current_sum - k]
            prefix_sums[current_sum] += 1

        return count