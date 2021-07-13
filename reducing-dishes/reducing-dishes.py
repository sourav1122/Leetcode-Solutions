class Solution:
    def maxSatisfaction(self, A):
        res = total = 0
        A.sort()
        while A and A[-1] + total > 0:
            total += A.pop()
            print(total,"klk")
            res += total
            print(total,A)
        return res
                