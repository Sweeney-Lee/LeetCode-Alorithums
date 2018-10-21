from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums):
        if not nums: return 0
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        length = 1
        for index in range(1, len(nums)):
            num = nums[index]
            if num < dp[0]:
                dp[0] = num
            elif num > dp[length-1]:
                dp[length] = num
                length += 1
            else:
                i = bisect_left(dp, num, 0, length)
                dp[i] = num
        return length

s = Solution()
a = s.lengthOfLIS([10,9,2,5,3,7,101,18])
print(a)