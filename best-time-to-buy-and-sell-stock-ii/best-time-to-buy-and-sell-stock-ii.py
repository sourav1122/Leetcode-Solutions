class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr=prices
        mini=99999
        miniindi=999999
        maxi=-1
        maxiindi=-1
        cost=0
        i=0
        for i in range(len(prices)-1):
            if prices[i+1]-prices[i]>0:
                cost+=prices[i+1]-prices[i]
        return cost
                  