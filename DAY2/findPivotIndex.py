class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #timeComplexity=O(N)
        #spaceComplexity=O(1)
        #find total sum
        totalSum=0
        for i in nums:
            totalSum=totalSum+i
        leftSum=0
        for i in range(len(nums)):
            #calculate right sum while tarversing through array and check if rightsum ==leftsum
            rightSum=totalSum-leftSum-nums[i]
            if rightSum==leftSum:
                return i
            
            leftSum=leftSum+nums[i]
        return -1 
        '''for i in range(len(nums)):
            if sum(nums[:i:])==sum(nums[i+1::]):
                return i
        return -1'''
        
    