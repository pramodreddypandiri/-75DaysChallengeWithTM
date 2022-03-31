class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #time compllexity=O(N**2)
        #space Complexity=O(1)
        '''output=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    output.append(i)
                    output.append(j)
                    break
        return output    '''
        #time compllexity=O(N)
        #space Complexity=O(N)(for using hashmap)
        output=[]
        #create a hashmap to store ele and its index
        hMap={}
        for i in range(0,len(nums)):
            #traverse the array and see for required ele in hashmap
            if (target-nums[i]) in hMap:
                output.append(i)
                output.append(hMap[target-nums[i]])
            hMap[nums[i]]=i
        return output    
                 
                    