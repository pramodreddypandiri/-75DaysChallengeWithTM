class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        #brute force solution : we can we extra array to get result
        #timeComplexity=O(N)
        #spaceComplexity=O(N)
        #Tow Pointer Approach
        #timeComplexity=O(N)
        #spaceComplexity=O(1)
        i=0
        j=0
        #traverse the array ,swap non-zeroes with zeroes
        while i<len(nums):
            if nums[i]!=0:
                nums[j],nums[i]=nums[i],nums[j]
                i=i+1
                j=j+1
            else:
                i=i+1
        return nums        