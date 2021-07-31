class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map=[]

    def insert(self, key: str, val: int) -> None:
        x=self.map
        p=0
        for i in range(len(x)):
            
            if x[i][0]==key:
                p=1
                x[i]=[key,val]
        if p!=1:
            x.append([key,val])
        #print(x)
        return x
    def sum(self, prefix: str) -> int:
        x=self.map
        
        ans=0
        for i in x:
            #print(i[0][:len(x)])
            if i[0][:len(prefix)]==prefix:
                ans+=i[1]
        #print(x,prefix,ans)
        return ans


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)