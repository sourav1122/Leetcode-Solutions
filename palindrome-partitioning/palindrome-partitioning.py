class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def palindrome(stri):
            #print(stri)
            if stri==stri[::-1]:
                return 1
            return 0
        ans=[]
        def solve(subs,val):
            #print(val,subs)
            if len(subs)==0:
                print(val,"KEHRY")
                ans.append(val)
                return
            for i in range(len(subs)):
                pref=subs[:i+1]
                rema=subs[i+1:]
                #print(pref,rema)
                if palindrome(pref):
                    
                    solve(rema,val+[pref])
        solve(s,[])
        return ans
                    
                
                
            