class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge=[0]*(len(nums2))
        st=[]
        nge[-1]=-1
        st.append(nums2[-1])
        n=len(nums2)
        for i in range(n-2,-1,-1):
            while(st!=[] and st[-1]<nums2[i]):
                st.pop(-1)
            if st==[]:
                nge[i]=-1
                st.append(nums2[i])
            else:
                nge[i]=st[-1]
                st.append(nums2[i])
        d={}
        j=0
        for i in nums2:
            d[i]=nge[j]
            j+=1
        ans=[]
        for i in nums1:
            ans.append(d[i])
        return ans
                
            
                