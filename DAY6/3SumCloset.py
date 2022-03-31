class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        #algorithms is almost* same as 3Sum
        #time=O(N**2)
        #space=O(1)
        nums.sort()
        mindiff=1000
        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                threeSum=a+nums[l]+nums[r]
                #claclulate three sum for every triplet
                #calculate diff b/w threesumma nd target
                diff=abs(threeSum-target)
                #if diff is min so far then update mindiff and ans
                if diff<mindiff:
                    mindiff=diff
                    ans=threeSum
                if threeSum>target:
                    r=r-1
                elif threeSum<target:
                    l=l+1
                else:
                    return target
                
        
        return ans
                    