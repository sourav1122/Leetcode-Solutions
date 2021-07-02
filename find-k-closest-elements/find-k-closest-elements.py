class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
            from heapq import heapify,heappush,heappop
            heap=[]
            heapify(heap)
            for i in arr:
                heappush(heap,[-abs(i-x),-i])
                if len(heap)>k:
                    heappop(heap)
            ans=[]
        
            for i in range(k):
                x=heappop(heap)
                ans.append(-x[1])
            return sorted(ans)
                
                