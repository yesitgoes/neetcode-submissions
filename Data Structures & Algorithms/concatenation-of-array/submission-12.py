class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # 1 4 1 2 1 4 1 2
        n = len(nums)
        ans = [0] * (2 * n)
        for i in range(n):
            ans[i] = ans[i + n] = nums[i]
        return ans
