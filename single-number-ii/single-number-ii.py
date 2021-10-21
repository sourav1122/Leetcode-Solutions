class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x=[0]*32
        for i in nums:
            i+=2**31
            r='{:032b}'.format(i)
            #if i<0:
            #    r=bin((1 << 32) - i)
            #     r=r[2:]
            for j in range(32):
                #print(r[j])
                if r[j]=='1':
                    #print("jaa")
                    x[j]+=1
        #print(x)
        for i in range(32):
            x[i]=x[i]%3
        x=[str(i) for i in x]
        #f=int("".join(x),2)-2**31
        #print(f)
        return int("".join(x),2)-2**31