class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    ans[0], ans[1] = i, j
        return ans