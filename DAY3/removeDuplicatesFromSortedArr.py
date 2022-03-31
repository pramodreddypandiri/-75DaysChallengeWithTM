class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #time-O(N)
        #space=O(1)
        i=1
        j=1
        #use two pointers
        while i<len(nums):
            #bypass similar elements with i pointer
            if nums[i]==nums[i-1]:
                i=i+1
            #assign unique ele at j pointer
            else:
                nums[j]=nums[i]
                j=j+1
                i=i+1
        return j
        '''*brute force
        create a set and make given array to set- time=O(N)+O(Nlog(N))
        now place set elements one by one at front of array-time=O(N)
        totalTime=O(N)+O(Nlog(N))+O(N)
        space=O(N) for set
        '''
        