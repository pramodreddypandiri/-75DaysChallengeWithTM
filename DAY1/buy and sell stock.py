class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #time complexity=O(N)
        #spaceComplexity=O(1)
        #take two pointers at the beginning
        maxProfit=0
        l=0
        r=1
        while  r<len(prices):
            #traverse until you find price greater than first pointer
            # and then calculate diff,if it is greater than maxProfit update maxProfit
            if prices[r]>prices[l]:
                profit=prices[r]-prices[l]
                maxProfit=max(maxProfit,profit)
            else:
                l=r
            
            r=r+1
        return maxProfit
    