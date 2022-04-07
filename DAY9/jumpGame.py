class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #greedy algorithm
        #time=O(N)
        #space=O(1)
        goal=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i]>=goal:
                goal=i
        return goal==0        