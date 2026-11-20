class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [prices[0]]

        for i in range(1, len(prices)):
            end = dp[-1]

            minPrice = min(prices[i], end)

            dp.append(minPrice)
            print(dp)

        res = -1

        for i in range(0, len(prices)):
            res = max(res, prices[i] - dp[i])

        return res

        
        