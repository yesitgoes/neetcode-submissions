class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for num in nums:
            mp[num] += 1
        ans = []
        for key, value in mp.items():
            ans.append([key, value])
        ans.sort(key = lambda x: x[1], reverse = True)
        ans1 = []
        for i in range(k):
            ans1.append(ans[i][0])
        return ans1
