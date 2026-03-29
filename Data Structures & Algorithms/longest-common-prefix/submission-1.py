class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Vertical scanning
        if not strs:
            return ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or c != s[i]:
                    return strs[0][:i]
        return strs[0]
        
