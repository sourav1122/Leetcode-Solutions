class Solution:
    def trap(self, height: List[int]) -> int:
        if height==[]:
            return 0
        l=[0]*(len(height))
        l[0]=height[0]
        for i in range(1,len(height)):
            l[i]=max(l[i-1],height[i])
        r=[0]*(len(height))
        r[len(height)-1]=height[-1]
        for i in range(len(height)-2,-1,-1):
            r[i]=max(r[i+1],height[i])
        ans=0
        for i in range(len(height)):
            ans+=min(l[i],r[i])-height[i]
        return ans        