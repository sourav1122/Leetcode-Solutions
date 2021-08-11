class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        d={}
        arr.sort()
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        if 0 in d:
            if d[0]%2!=0:
                return 0
            d[0]=0
        for i in range(len(arr)) :
            #print(arr[i])
            if arr[i]==0:
                continue
            #print(  arr[i],"YAHA")
            if 2*arr[i] not in d and  arr[i]//2 not in d:
                #print("YAHA")
                return 0
            if 2*arr[i] in d and d[arr[i]]!=0 and d[2*arr[i]]!=0:
                x=min(d[2*arr[i]],d[arr[i]])
                d[2*arr[i]]-=x
                d[arr[i]]-=x
            elif arr[i]//2 in d and d[arr[i]]!=0 and d[arr[i]//2]!=0:
                x=min(d[arr[i]//2],d[arr[i]])
                d[arr[i]//2]-=x
                d[arr[i]]-=x
            #print(d)
        #print(d)
        for i in d:
            if d[i]!=0:
                return 0
        return 1
                
                
                
            
            
        