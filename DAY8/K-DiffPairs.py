class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        #time=O(Nlog(N)) for sorting +O(N*log(N)) for traversal and binary search
        #space=O(1)
        count=0
        nums.sort()
        #fix first one of pairs and do binary search for target in rest of the array
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]<(nums[i]+k):
                    l=mid+1
                elif nums[mid]>(nums[i]+k):
                    r=mid-1
                else:
                    count=count+1
                    break
                
        return count
    
            