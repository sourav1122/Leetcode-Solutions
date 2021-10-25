class MinStack:

    def __init__(self):
        self.s1=[]
        self.s2=[]

    def push(self, val: int) -> None:
        self.s1.append(val)
        if self.s2==[]:
            self.s2.append(val)
        elif self.s1[-1]<=self.s2[-1]:
            self.s2.append(val)
        

    def pop(self) -> None:
        #print(self.s1,self.s2,"YAHA")
        if self.s2!=[]:
            if self.s1[-1]==self.s2[-1]:
                #print(self.s1[-1],"KKK")
                self.s1.pop(-1)
                self.s2.pop(-1)
            else:
                self.s1.pop(-1) 
        else:
            self.s1.pop(-1)        
    def top(self) -> int:
        x=self.s1[-1]
        return x         
        

    def getMin(self) -> int:
        #print(self.s2)
        if self.s2==[]:
            return 0
        x=self.s2[-1]
        return x
    
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()