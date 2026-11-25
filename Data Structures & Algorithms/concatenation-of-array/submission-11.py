class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # 1 4 1 2 1 4 1 2
        n = len(nums)
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans
