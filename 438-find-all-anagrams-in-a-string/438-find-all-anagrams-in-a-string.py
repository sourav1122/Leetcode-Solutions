class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sw=[0]*(26)
        if len(p)>len(s):
            return []
        for i in p:
            sw[ord(i)-ord('a')]+=1
        tms=[0]*26
        for i in range(len(p)):
            tms[ord(s[i])-ord('a')]+=1
        fs=[]
        if tms==sw:
            fs.append(0)
        for i in range(len(p),len(s)):
            
            tms[ord(s[i-(len(p))])-ord('a')]-=1
            tms[ord(s[i])-ord('a')]+=1
            #print(tms,s[i])
            #print(sw)
            if sw==tms:
                #print("HAAA",i)
                #print(tms,s[i])
                #print(sw)
                fs.append(i-(len(p)-1))
        return fs
            
        