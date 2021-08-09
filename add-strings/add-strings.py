class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        while(len(num2)!=len(num1)):
            if len(num2)<len(num1):
                num2='0'+num2
            if len(num1)<len(num2):
                num1='0'+num1
        hacil='0'
        ans=""
        for i in range(len(num1)-1,-1,-1):
            x=ord(num1[i])
            y=ord(num2[i])
            f=x+y+ord(hacil)-48-48
            hacil='0'
            if f>57:
                remainder=f-57
                r='1'+chr(remainder+48-1)
            else:
                r=chr(f)
            if len(r)>1:
                g=r[1]
                ans=g+ans
                hacil=r[0]
            else:
                ans=r+ans
        if hacil=='0':
            return ans
        return hacil+ans
        
            
            
            