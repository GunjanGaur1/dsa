class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        hash = {}
        for num in nums:
            if num not in hash:
                hash[num]=1
            else:
                hash[num]+=1
        print(hash)
        longest=0
        for current in hash:
            if current-1 not in hash:
                count=1
                while current+1 in hash:
                    current=current+1
                    count=count+1
                longest = max(longest,count)
        return longest
            