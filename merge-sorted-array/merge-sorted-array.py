class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr=[0]*(m+n)
        k=0
        i=0
        j=0
        while(i<m and j<n):
            if nums1[i]<=nums2[j]:
                arr[k]=nums1[i]
                i+=1
                k+=1
                #print(nums1,"updar")
            elif nums2[j]<=nums1[i]:
                arr[k]=nums2[j]
                k+=1
                j+=1
            #print(nums1,"niche")
            #print(i,j,"YAHA")
        if (i<m):
            while(i!=m):
                arr[k]=nums1[i]
                i+=1
                k+=1
        if (j<n):
            while(j!=n):
                arr[k]=nums2[j]
                j+=1
                k+=1
        nums1[:m+n] = arr[:m+n]
        