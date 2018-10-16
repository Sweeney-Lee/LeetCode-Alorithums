class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        temp = 0
        for i in range(1, len(prices)):
            temp += prices[i] - prices[i - 1]
            temp = temp if temp >= 0 else 0
            result = max(temp, result)
        return result

s = Solution()
a = s.maxProfit([7,6,4,3,1])
print(a)