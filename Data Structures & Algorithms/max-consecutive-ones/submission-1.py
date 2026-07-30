class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        arr = []
        arr.append(nums[0])
        for i in range(1, n):
            if nums[i] == 1:
                if nums[i - 1] == 1:
                    arr.append(arr[i - 1] + 1)
                else:
                    arr.append(1)
            else:
                arr.append(0)
        return max(arr)
