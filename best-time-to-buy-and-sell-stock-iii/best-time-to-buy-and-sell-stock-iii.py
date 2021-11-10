class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min1=9999999
        p1=0
        min2=9999999
        p2=0
        for i in range(len(prices)):
            min1=min(min1,prices[i])
            p1=max(p1,prices[i]-min1)
            min2=min(min2,prices[i]-p1)
            p2=max(p2,prices[i]-min2)
        return p2