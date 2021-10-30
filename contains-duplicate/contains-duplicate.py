class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=set()
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                return 1
        return 0