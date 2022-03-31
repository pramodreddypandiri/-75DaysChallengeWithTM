class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''**brute-force
        pick elements and count occurance of element in rest of the array,return if count is as asked
        time=O(N**2)
        space=O(1)
        '''
        
        """**better 
        #create hashmap and add ele and its frequency
        #time=O(N)+O(Nlog(N))+O(N)
        #space=O(N)
        hMap={}
        n=len(nums)
        #O(N)
        for i in range(n):
            #searching takes O(Nlog(N))
            if nums[i] in hMap:
                hMap[nums[i]]+=1
            else:
                hMap[nums[i]]=1
        #return ele if its frequency is as asked
        #O(N)
        for i in hMap:
            if hMap[i]>n//2:
                return i
        return -1  """
        '''**optimal'''
        #moore voting algorythm
        #time=O(N)
        #space=O(1)
        ele=0
        count=0
        for i in range(len(nums)):
            if count==0:
                ele=nums[i]
            if ele==nums[i]:count+=1
            else:count-=1
                
        return ele            
        