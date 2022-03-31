class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==0 or len(nums)==1:
            return 0
        '''count=0
        p=0
        while p<len(nums)-1:
            if nums[p]<nums[p+1]:
                p=p+1
                count=count+1
            elif nums[p]>nums[p+1]:
                p=p+nums[p]
                count=count+1
            else:
                p=p+nums[p]
                count=count+1
        return count'''
        '''dp=[10000 for i in range(len(nums))]
        dp[0]=0
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[j]+j>=i:
                    dp[i]=min(dp[i],dp[j]+1)
        return dp[-1] '''
        #kind of BFS algo
        #time=O(N) O(N**2) in worst case
        #space=O(1)
        res=0
        l,r=0,0
        while r<len(nums)-1:
            farthestIndex=0
            for i in range(l,r+1):
                farthestIndex=max(farthestIndex,i+nums[i])
            l=r+1
            r=farthestIndex
            res+=1
        return res    
    
        