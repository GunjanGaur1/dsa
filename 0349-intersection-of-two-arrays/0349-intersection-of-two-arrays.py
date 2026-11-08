class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n = len(nums1)
        m = len(nums2)
        hash={}
        hash1={}
        result=[]

        for i in range(n):
            if nums1[i] in hash:
                hash[nums1[i]] = i
            else:
                hash[nums1[i]] = 1
        for num in nums2:
            if num in hash:
                result.append(num)
                del hash[num]
        return result
            