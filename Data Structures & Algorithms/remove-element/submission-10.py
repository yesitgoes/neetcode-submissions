class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 3 2 2 3 : 3
        # 2 2 -> 2

        # 0 1 2 2 3 0 4 2 : 2
        # 0 1 3 0 4 -> 5

        # for 
        # same -> skip diff -> keep
        # for
        # overwrite
        # return len list
        # sp: n

        l = []
        for num in nums:
            if num == val:
                continue
            else:
                l.append(num)
        n = len(l)
        for i in range(n):
            nums[i] = l[i]
        return n
