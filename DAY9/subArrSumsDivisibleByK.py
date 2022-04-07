class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        #time=O(N)
        #space=O(N)
        ans=0
        prefix=0
        #create an array(count) to count and store remainders 
        count=[1]+[0]*k
        for i in nums:
            #as we move forward in array calculate remainder till then ans store
            prefix=(prefix+i)%k
            #add to ans 
            ans+=count[prefix]
            count[prefix]+=1
        return ans    
        