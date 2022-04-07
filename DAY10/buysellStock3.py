class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit1=0
        currMin1=1000000
        profit2=0
        currMin2=1000000
        for i in range(len(prices)):
            currMin1=min(prices[i],currMin1)
            profit1=max(profit1,prices[i]-currMin1)
            currMin2=min(currMin2,prices[i]-profit1)
            profit2=max(profit2,prices[i]-currMin2)
        return profit2    