class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        for item in strs:
            key=tuple(sorted(item))

            if key not in seen:
                seen[key]=[]
            seen[key].append(item)
        return list(seen.values())