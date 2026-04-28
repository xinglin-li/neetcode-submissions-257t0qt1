class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        res = [1]*n
        #从左到右, 保证右边更高时, 右边比左边多
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1
        #从右到左, 保证左边更高时, 左边比右边多
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                res[i] = max(res[i], res[i+1]+1)

        return sum(res)

