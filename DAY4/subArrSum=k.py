class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''*brute force
        time=O(N**2)
        space=O(1)
        count=0
        for i in range(len(nums)+1):
            for j in range(i):
                if sum(nums[j:i])==k:
                    
                    count+=1
                    
                
       
        return count'''
        '''count=0
        i=0
        j=0
        while i<len(nums) and j<len(nums):
            if sum(nums[i:j])==k:
                count+=1
            elif sum(nums[i:j])<k:
                j=j+1
            elif sum(nums[i:j])>k:
                i=i+1
                j=i
        return count '''
        '''*optimal
        time=O(N)
        space=O(N)'''
        count=0
        hMap={0:1}
        currSum=0
        #iterate and calcute curr sum
        for n in nums:
            currSum=currSum+n
            #calcute diff to know if there is a prefix sum that would add to count
            diff=currSum-k
            count=count+hMap.get(diff,0)#get fun return 0 if there is no key
            #add currSum and its frequency to hashmap
            hMap[currSum]=hMap.get(currSum,0)+1
        return count    
            