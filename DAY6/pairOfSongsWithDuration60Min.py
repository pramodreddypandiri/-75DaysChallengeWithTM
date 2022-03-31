class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        '''#*Brute
        #time=O(N**2)
        #space=O(1)
        count=0
        for i in range(len(time)-1):
            for j in range(i+1,len(time)):
                if (time[i]+time[j])%60==0:
                    count+=1
        return count
        '''
        #time=O(N)
        #space=O(1)
        #create a frequency array to store remainder's count
        freqArr=[0]*60
        for i in time:
            freqArr[i%60]+=1
        ans=0
        for i in range(1,len(freqArr)//2):
            #traverse the freq arr check for correct pairs and add their product to ans
            ans+=freqArr[i]*freqArr[60-i]
        #edge cases for remainder 0 and 30
        ans=ans+(freqArr[0]*(freqArr[0]-1)//2)+(freqArr[30]*(freqArr[30]-1)//2)
        return ans
    