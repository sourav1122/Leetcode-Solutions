class Solution {
public:
    int maxPower(string s) {
        int lcal=0;
        int mcal=0;
        if (s.size()==1){
            return 1;
        }
        for (int i=1;i<s.size();i++){
            if (s[i]==s[i-1]){
                lcal+=1;
            }
            else{
                mcal=max(lcal+1,mcal);
                lcal=0;
                
            }
        }
        mcal=max(lcal+1,mcal);
        return mcal;
    }
    
};