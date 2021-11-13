class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int cs=coins.size();
        int dp[amount+1];
        dp[0]=0;
        int INF=100000000;
        int inf=INF;
        for (int i=1;i<=amount;i++){
            dp[i]=INF;
            int ans=inf;
            for(int j=0;j<cs;j++){
              if(coins[j]<=i)
                ans=min(ans,dp[i-coins[j]]);
                
            }
            if (ans==INF)
            {
                dp[i]=INF;
                
            }
            else{
                dp[i]=ans+1;
            }
        }
        
        if(dp[amount]==INF){
            return -1;
        }
        else{
            return dp[amount];
        }
        
    }
};