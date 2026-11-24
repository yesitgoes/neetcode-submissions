class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # 1 1 0 1 1 1
        # 1 2 0 1 2 3 
        # 3
        # for 
        # if 1 cnt += 1 if 0 cnt = 0
        # cnt = max cnt 

        ans, cnt = 0, 0
        for num in nums:
            if num == 1:
                cnt += 1
            elif num == 0:
                cnt = 0
            ans = max(ans, cnt)
        return ans  
         

