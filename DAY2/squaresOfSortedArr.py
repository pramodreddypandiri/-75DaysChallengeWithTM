class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #timeComplexity=O(N)
        #spaceComplexity=O(N)
        #take output for storing squares of elements
        outPut=[0]*len(nums)
        #take two pointers,compare left and right,add to output array accordingly
        l=0
        r=len(nums)-1
        i=len(nums)-1
        while l<=r:
            if nums[r]*nums[r]>nums[l]*nums[l]:
                outPut[i]=nums[r]*nums[r]
                i=i-1
                r=r-1
            else:
                outPut[i]=nums[l]*nums[l]
                i=i-1
                l=l+1
        return outPut
        