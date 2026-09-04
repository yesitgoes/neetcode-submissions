class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = [0] * len(nums)
        n = 1
        for num in nums:
            n *= num
            prefix.append(n)
        n = 1
        for i in range(len(nums) - 1, -1, -1):
            n *= nums[i]
            postfix[i] = n
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(postfix[i + 1])
            elif i == len(nums) - 1:
                res.append(prefix[i - 1])
            else:
                res.append(prefix[i - 1] * postfix[i + 1])
        return res
            