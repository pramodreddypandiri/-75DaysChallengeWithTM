class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''*brute force: run three loops
        time=O(N**3)
        space=O(N)

        '''
        '''**better:sort the array,pick one ele and solve for twoSum in the rest of the array
        '''
        #optimal-solution
        #time=O(Nlog(N))+O(N)+O(log(N))
        #space=O(N)
        output=[]
        #sort the given array
        nums.sort()#O(Nlog(N))
        #pick one element i.e (a)
        for i,a in enumerate(nums):#O(N)
            #skip elements if there are duplicates ,to avoid similar triplets
            if i>0 and a==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            #search for target sum in the remaining array using two pointers(b&c)
            while l<r:#O(log(N))
                targetSum=a+nums[l]+nums[r]
                if targetSum>0:
                    r=r-1
                elif targetSum<0:
                    l=l+1
                else:
                    output.append([a,nums[l],nums[r]])
                    l=l+1
                    #r=r-1
                    #after getting a triplet move left pointer till you get different a value to avoid duplicate triplets
                    while nums[l]==nums[l-1] and l<r:
                        l=l+1
                    
                
                #while nums[r]==nums[r-1]:
                    #r=r-1
        return output
    
            
            