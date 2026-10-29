class Solution:
    def minOperations(self, nums: List[int]) -> int:
        hash = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in hash:
                hash[nums[i]]=hash[nums[i]]+1
            else:
                hash[nums[i]]=1
        operations=0
        for freq in hash.values():
            if freq%3==0:
                operations += freq // 3
            elif freq % 3 == 2:
                operations += freq // 3 + 1
            else:
                if freq==1:
                    return -1
                else:
                    operations += (freq // 3) - 1 + 2
        return operations