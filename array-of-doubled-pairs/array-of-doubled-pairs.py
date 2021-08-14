class Solution(object):
    def canReorderDoubled(self, A):
        count = collections.Counter(A)
        print(count)
        for x in sorted(A, key = abs):
            print(x)
            if count[x] == 0: continue
            if count[2*x] == 0: return False
            count[x] -= 1
            count[2*x] -= 1

        return True