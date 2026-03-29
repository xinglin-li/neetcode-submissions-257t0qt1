class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_len = cur_len = 1
        for i in range(1,len(arr)):
            if arr[i] != arr[i-1]:
                if cur_len > 1:
                    if (arr[i-1] - arr[i-2] > 0 and arr[i] - arr[i-1] < 0) or (arr[i-1] - arr[i-2] < 0 and arr[i] - arr[i-1] > 0):
                        cur_len += 1
                        max_len = max(max_len,cur_len)
                    else:
                        cur_len = 2
                else:
                    cur_len += 1
                    max_len = max(max_len,cur_len)
            else:
                cur_len = 1
        return max_len