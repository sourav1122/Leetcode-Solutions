class Solution:
    def customSortString(self, order: str, str: str) -> str:
        d={}
        for i in range(len(order)):
            d[order[i]]=i+1
        d1={}
        
        for i in range(1,27):
            d1[i]=[]
        #print(d,d1)
        baaki=[]
        for char in str:
            if char in d:
                #print(d[char])
                d1[d[char]].append(char)
            else:
                baaki.append(char)
        ans=""
        for i in d1:
            ans+="".join(d1[i])
        ans+="".join(baaki)
        return ans