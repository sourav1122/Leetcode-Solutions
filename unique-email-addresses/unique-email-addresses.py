class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        d={}
        for i in range(len(emails)):
            f=list(emails[i])
            r=""
            for j in range(len(f)):
                if f[j]=="+"or f[j]=="@":
                    break
                else:
                    if f[j]==".":
                        continue
                    else:
                        r+=f[j]
            #print(f[j],j)
            while(f[j]!="@"):
                j+=1
            for g in range(j,len(f)):
                r+=f[g]
            if r not in d:
                d[r]=1
            else:
                d[r]+=1
        #print(d)
        return len(d)
                
            
                