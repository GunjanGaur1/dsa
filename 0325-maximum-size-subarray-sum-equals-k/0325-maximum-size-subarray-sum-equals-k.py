class Solution:
    def maxSubArrayLen(self, nums: list[int], k: int) -> int:
        n = len(nums)
        hashmap = {0: -1}
        prefix_sum = 0
        max_len = 0
        
        for i in range(len(nums)):
            prefix_sum += nums[i]

            if prefix_sum - k in hashmap:
                max_len = max(max_len,i-hashmap[prefix_sum-k])
            if prefix_sum  not in hashmap:
                hashmap[prefix_sum] = i

        return max_len
