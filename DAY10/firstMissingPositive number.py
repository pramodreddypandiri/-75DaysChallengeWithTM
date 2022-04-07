class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''my approach did not work for test cases with only negative numbers
        nums.sort()
        k=0
        while k<len(nums) :
            if nums[k]<=0:
                k=k+1
            else:
                break
        if k<len(nums):
            if nums[k]>1:
                return 1
            while k<len(nums)-1:
                if nums[k+1]==nums[k]+1:
                    k=k+1
                else:
                    return nums[k]+1
        return nums[-1]+1    
            '''
        #time=O(nlogn)+O(n)
        #space(1)
        nums.sort()
        ans=1
        #ans will remain 1 till yor reach 1 in array
        #if you reach 1 ,ans will increase by 1  for every loop, ans will stop incrementing if we miss a number (i.e actual missing number) 
        for i in nums:
            if i==ans:
                ans=ans+1
                
        return ans        
        