class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        '''my first sol, did not work 
        if k>len(cardPoints):
            return
        #if k==len(cardPoints):
          #  return sum(cardPoints)
        
        l=0
        r=len(cardPoints)-1
        total=0
        while l<=r and k>0:
            if cardPoints[r]>=cardPoints[l]:
                total=total+cardPoints[r]
                k=k-1
                r=r-1
            elif cardPoints[r]<cardPoints[l]:
                total=total+cardPoints[l]
                k=k-1
                l=l+1
        return total '''
        #sliding window method
        #time=O(N)
        #spaceO(1)
        l=0
        r=len(cardPoints)-k
        total=sum(cardPoints[r:])
        res=total
        while r<len(cardPoints):
            #move window and check for maxtotal(res)
            total=total+(cardPoints[l]-cardPoints[r])
            res=max(res,total)
            r=r+1
            l=l+1
        return res    
            