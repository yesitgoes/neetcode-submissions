class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tmp = []
        for num in nums:
            if num == val:
                continue
            else:
                tmp.append(num)
        ans = len(tmp)
        for i in range(ans):
            nums[i] = tmp[i]
        return ans

            