class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()# sort the fiven array
        verticalCuts.sort()#sort the fiven array
        hCuts=[0]
        
        #make new  horizontal array with 0 and h as its extremes
        for i in horizontalCuts:
            hCuts.append(i)
        hCuts.append(h)
        #make new  vertical array with 0 and w as its extremes
        vCuts=[0]
        for i in verticalCuts:
            vCuts.append(i)
        vCuts.append(w)
        maxH=0
        #calcuate max diff b/w horizontal lines 
        for i in range(1,len(hCuts)):
            maxH=max(maxH,(hCuts[i]-hCuts[i-1]))
        maxV=0
        #calcuate max diff b/w vertical lines 
        for i in range(1,len(vCuts)):
            maxV=max(maxV,(vCuts[i]-vCuts[i-1]))
        #product is the area
        area=maxH*maxV
        return area%((10**9)+7)
        