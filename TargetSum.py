class Solution:

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        d = {}

        if not nums:
            return 0

        def dfs(sum, idx):
            if (sum, idx) in d:
                return d[(sum, idx)]
            if idx == len(nums):
                ans = None
                if sum == 0:
                    ans = 1
                else:
                    ans = 0
                d[(sum, idx)] = ans
                return d[(sum, idx)]

            d[(sum, idx)] = dfs(sum - nums[idx], idx + 1) + dfs(sum + nums[idx], idx + 1)
            return d[(sum, idx)]

        return dfs(S, 0)