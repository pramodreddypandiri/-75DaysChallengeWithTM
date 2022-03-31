class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        '''res=[]
        for i in nums:
            if nums.count(i)==2:
                res.append(i)
        return set(res)        
    '''
        '''*brute force
        time=O(N)+O(Nlog(N))
        space=O(1)
        res=[]
        nums.sort()
        if len(nums)==1:
            return res
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                res.append(nums[i])
        return set(res)'''
        '''#time=O(N)+O(N)
        #space=O(N)
        hMap={}
        for i in nums:
            if i in hMap:
                hMap[i]+=1
            else:
                hMap[i]=1
        ans=[]
        for i in hMap:
            if hMap[i]>1:
                ans.append(i)
        return ans  '''
        #time=O(N)
        #space=O(1)
        #*optimal
        ans=[]
        #since all number are b/w 1 to n 
        #we traverse the array,put negative value at nums[abs(n)-1] so that we mark it as visited
        #if there is a duplicate we will encounter negative number at nums[abs(n)-1] so we add it to output
        for n in nums:
            if nums[abs(n)-1]<0:
                ans.append(abs(n))
            else:
                nums[abs(n)-1]=-1*nums[abs(n)-1]
                
        return ans    
    