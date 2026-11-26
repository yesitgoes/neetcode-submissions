class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # N = len(nums)
        # for i in range(N):
        #     for j in range(i + 1, N):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        N = len(nums)
        mp = {}
        for i in range(N):
            tmp = target - nums[i] # tmp + nums[i] == target
            # print(nums[i], tmp, mp)
            if tmp in mp:
                return [mp[tmp], i]
            else:
                mp[nums[i]] = i
        


