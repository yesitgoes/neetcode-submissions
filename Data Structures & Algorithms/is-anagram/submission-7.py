class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_mp = {}
        t_mp = {}
        for c in s:
            s_mp[c] = s_mp.get(c, 0) + 1
        for c in t:
            t_mp[c] = t_mp.get(c, 0) + 1
        return t_mp == s_mp