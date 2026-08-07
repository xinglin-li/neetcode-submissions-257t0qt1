class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
         # 当前位置能不能到达，取决于前面一个滑动窗口中是否存在 reachable position。
         # 维护的滑动窗口是能跳到位置i的窗口. [i - maxJump, i - minJump]
         # 为了移动到 [i - maxJump, i - minJump], i - maxJump - 1 被移除, i - minJump 进来
        n = len(s)
        dp = [False] * n
        dp[0] = True

        reachable = 0

        for i in range(1, n):
            if i - minJump >= 0 and dp[i - minJump]:
                reachable += 1

            if i - maxJump - 1 >= 0 and dp[i - maxJump - 1]:
                reachable -= 1

            dp[i] = (s[i] == "0" and reachable > 0)

        return dp[-1]
        

