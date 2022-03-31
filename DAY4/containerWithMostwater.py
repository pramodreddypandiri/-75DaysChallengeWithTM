class Solution:
    def maxArea(self, height: List[int]) -> int:
        #two pointer approach
        #time=O(N) in worst case
        #space=O(1)
        l=0
        r=len(height)-1
        maxArea=0
        while l<r:
            #calculate and comapare with maxArea
            maxArea=max(maxArea,(min(height[l],height[r])*(r-l)))
            #move the pointer of minimum height
            if height[l]<height[r]:
                l=l+1
            else:
                r=r-1
        return maxArea        
        