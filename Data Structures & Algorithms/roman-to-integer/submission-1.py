class Solution:
    def romanToInt(self, s: str) -> int:
        numeral_map = {"I":1,"V":5,"X":10,
        "L":50,"C":100,"D":500,"M":1000}
        n = len(s)
        if n == 1:
            return numeral_map[s]
        sum = 0
        for i in range(n):
            if i < n - 1 and numeral_map[s[i]] < numeral_map[s[i+1]]:
                sum -= numeral_map[s[i]]
            else:
                sum += numeral_map[s[i]]
        return sum

