class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bsp=-prices[0]
        csp=0
        ssp=0
        for i in range(1,len(prices)):
            nbsp=0
            nssp=0
            ncsp=0
            if csp-prices[i]>bsp:
                nbsp=csp-prices[i]
            else:
                nbsp=bsp
            if ssp>csp:
                ncsp=ssp
            else:
                ncsp=csp
            if bsp+prices[i]>ssp:
                nssp=bsp+prices[i]
            else:
                nssp=ssp
            ssp=nssp
            bsp=nbsp
            csp=ncsp
        return ssp