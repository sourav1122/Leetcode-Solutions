class Solution:
    def minCut(self, s: str) -> int:
        if not s : return 0
        dp = [[True] * len(s) for i in range(len(s))] 
        cuts = [float("inf")] * len(s)
        for r in range(1, len(s)):
            for c in range(len(s) - r):
                if not (s[c] == s[c + r] and dp[c + 1][c + r - 1]):
                    dp[c][c + r] = False
        for i in range(len(s)):
            for j in range(i + 1):
                if dp[j][i]:
                    cuts[i] = min(cuts[i], (cuts[j - 1] + 1) if j - 1 >= 0 else 0)
                    
        return cuts[-1]