class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen_s={}
        seen_t={}
        for ch in s:
            if ch in seen_s:
                seen_s[ch]+=1
            else:
                seen_s[ch]=1
        for ch in t:
            if ch in seen_t:
                seen_t[ch]+=1
            else:
                seen_t[ch]=1
        for item in seen_s:
            if item not in seen_t:
                return False
            elif seen_s[item]!=seen_t[item]:
                return False
        return True