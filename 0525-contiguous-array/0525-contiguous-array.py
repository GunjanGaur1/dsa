class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hash = {0:-1}
        prefix_sum = 0
        max_len = 0

        n = len(nums)
        for i in range(n):
            if nums[i]==1:
                prefix_sum = prefix_sum + 1 
            else:
                prefix_sum = prefix_sum -1

            if prefix_sum in hash:
                max_len = max(max_len,i-hash[prefix_sum])
            else:
                hash[prefix_sum] = i


        return max_len

        