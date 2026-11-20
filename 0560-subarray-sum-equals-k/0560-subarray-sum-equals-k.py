class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        count=0
        hash = {0:1}
        prefix=0

        for num in nums:
            prefix = prefix+num
            if prefix-k in hash:
                count=count+hash[prefix-k]
            hash[prefix] = hash.get(prefix, 0) + 1
        return count

        