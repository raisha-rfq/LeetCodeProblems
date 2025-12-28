class Solution:
    def twoSum(self, num, target):
        final = {}
        for i, n in enumerate(num):
            s = target - n
            if s in final:
                return(final[s], i)
            final[n] = i


sol = Solution()
num = [3,2,4]
target = 6
print(sol.twoSum(num, target))
