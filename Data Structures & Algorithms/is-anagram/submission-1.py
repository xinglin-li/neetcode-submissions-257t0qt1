class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            s_i = s[i]
            t_i = t[i]
            if s_i in s_dict:
                s_dict[s_i] += 1
            else:
                s_dict[s_i] = 1
            
            if t_i in t_dict:
                t_dict[t_i] += 1
            else:
                t_dict[t_i] = 1
        
        for k,v in s_dict.items():
            if k not in t_dict:
                return False
            elif t_dict[k] == s_dict[k]:
                continue
            else:
                return False
        return True
        