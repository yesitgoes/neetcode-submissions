class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] == val:
                nums[i] = 101
        nums.sort()
        k = 0
        for num in nums:
            if num == 101:
                break
            k += 1
        return k