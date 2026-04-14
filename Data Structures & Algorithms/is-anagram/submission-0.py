class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
          return False

        ds,dt = {},{}
        for i in range(len(s)):
          ds[s[i]] = s.count(s[i])
          dt[t[i]] = t.count(t[i])
        
        if ds == dt:
          return True
        else:
          return False 