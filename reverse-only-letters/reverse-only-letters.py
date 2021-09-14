class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        r=list(s)
        #print(r)
        i=0
        j=len(s)-1
        #print(r[i].isupper())
        while(i<j):
            #print(i,j,r[i],r[j])
            if ((r[i].isupper()==True or r[i].islower()==True) and (r[j].isupper()==True or r[j].islower()==True)):
                #print(i,j,r[i],r[j],"yahaa")
                r[i],r[j]=r[j],r[i]
                i+=1
                j-=1
            if (r[i].isupper()==False and r[i].islower()==False):
                #print(r[i],"YAHHHHHH")
                i+=1
            if (r[j].isupper()==False and r[j].islower()==False):
                #print(r[j],"YAHHHHHH")
                j-=1            
        return "".join(r)
                
                
                
                