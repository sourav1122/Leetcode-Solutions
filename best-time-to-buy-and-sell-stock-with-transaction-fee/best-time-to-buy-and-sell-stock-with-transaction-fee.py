class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        bsp=-prices[0]
        ssp=0
        for i in range(1,len(prices)):
            nbsp=0
            nssp=0
            if ssp-prices[i]>bsp:
                nbsp=ssp-prices[i]
            else:
                nbsp=bsp
            if bsp+prices[i]-fee>ssp:
                nssp=bsp+prices[i]-fee
            else:
                nssp=ssp
            ssp=nssp
            bsp=nbsp
        return ssp
                

                
        
        