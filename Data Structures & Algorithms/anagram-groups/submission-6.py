class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        ans = []
        for s in strs:
            # mp[''.join(sorted(s))].append(s)
            mp[tuple(sorted(s))].append(s)
            
            
        for value in mp.values():
            
            ans.append(value)
        return ans
