class Solution:
    def sortColors(self, nums: list[int]) -> None:
        n = len(nums)
        count=0
        count1=0
        count2=0
        for i in range(n):
            if nums[i]==0:
                count=count+1
                
            elif nums[i]==1:
                count1=count1+1
                
            else:
                count2=count2+1
            
        print(count)
        print(count1)
        print(count2)

        k = 0
        while k<count:
            nums[k]=0
            k=k+1
        
        while k<count+count1:
            nums[k]=1
            k=k+1
        
        while k<count+count1+count2:
            nums[k]=2
            k=k+1

        
            

        