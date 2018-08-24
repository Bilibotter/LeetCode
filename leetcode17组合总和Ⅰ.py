class Solution:
    def combinationSum(self, candidates, target):
        self.result = []
        candidates.sort()
        self.combinationsum(candidates, target, [])

        return self.result

    def combinationsum(self, candidates, remain, stack):
        for num, candidate in enumerate(candidates):
            if candidate < remain:
                self.combinationsum(candidates[num:], remain-candidate, stack+[candidate])
            elif candidate == remain:
                stack.append(candidate)
                self.result.append(stack)
                return
            else:
                return


s = Solution()
print(s.combinationSum([2,3,6,7],7))