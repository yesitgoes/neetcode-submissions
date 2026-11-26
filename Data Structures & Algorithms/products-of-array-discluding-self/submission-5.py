class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # nums = [1] + nums + [1]

        N = len(nums)

        pre = [1] * N 
        suff = [1] * N

        for i in range(1, N):
            pre[i] = pre[i - 1] * nums[i - 1]
        for i in range(N - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i + 1]

        ans = [1] * N
        for i in range(N):
            ans[i] = pre[i] * suff[i]
        return ans