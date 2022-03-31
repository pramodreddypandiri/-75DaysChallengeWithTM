class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''*my tried version-did not work for all test cases
        intervals.sort()
        outPut=[]
        k=0
        for i in range(len(intervals)):
            if  (i+1)<len(intervals) and intervals[(i+1)][0]<=intervals[i][-1]:
                continue
            else:
                outPut.append([intervals[k][0],intervals[i][-1]])
                k=i+1
        return outPut'''
        '''*brute-force
        sort intervals,pick first interval ans search for interval that can merge with firt one 
        time=O(Nlog(N)) for sorting+O(N**2) for searching
        space=O(N)
        '''
        #time-O(Nlog(N))+O(N)
        #space=O(N) in worst case for output array
        #sort intervals based on start value
        intervals.sort(key =lambda x: x[0])#O(Nlog(N))
        outPut=[]
        for i in intervals:#O(N)
            # if output is empty or end time of last interval in output < start time of current interval then append it to output
            if not outPut or outPut[-1][-1]<i[0]:
                outPut.append(i)
            else:
                #upadte the maximum of last end time in output and present end time in current interval 
                outPut[-1][-1]=max(i[-1],outPut[-1][-1])
        return outPut        
                
    
                