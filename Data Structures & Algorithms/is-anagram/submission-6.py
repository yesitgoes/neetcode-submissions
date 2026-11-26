class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_mp = defaultdict(int)
        t_mp = defaultdict(int)
        for c in s:
            s_mp[c] += 1
        for c in t:
            t_mp[c] += 1
        return t_mp == s_mp