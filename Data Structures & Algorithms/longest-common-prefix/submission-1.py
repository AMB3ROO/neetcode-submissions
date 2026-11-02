class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ref=min(strs, key=len)
        ans=""
        for i in range(len(ref)):
            for item in strs:
                if ref[i]!=item[i]:
                    break
            else:
                ans+=ref[i]
                continue
            break
        return ans