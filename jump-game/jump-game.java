class Solution {
    int[] dp = new int[10000 + 1];
    
    private boolean reachLast(int[] nums, int curIdx) {
        if (curIdx == nums.length - 1)
            return true;   
        if (curIdx < 0 || curIdx >= nums.length || nums[curIdx] == 0)
            return false;
        
        if (dp[curIdx] != -1)
            return (dp[curIdx] == 1 ? true : false);
        
        boolean result = false;
        for (int i = 1; i <= nums[curIdx]; i++)
            result = result || reachLast(nums, curIdx + i);    
        dp[curIdx] = (result ? 1 : 0);
        return result;
    }
    
    public boolean canJump(int[] nums) {
        Arrays.fill(dp, -1);
        return reachLast(nums, 0);
    }
}