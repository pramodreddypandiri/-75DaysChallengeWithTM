class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #timeComplexity=O(N)
        #spaceComplexity=O(1)
        #calculate profit for every increase in price and add it to profit
        profit=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profit+=(prices[i]-prices[i-1])
        return profit
        