class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob = 0
        notrob = 0
        for i in range(len(nums)):
            currob = notrob + nums[i]
            notrob = max(notrob, rob)
            rob = currob
        return max(rob, notrob)

s = Solution()
a = s.rob([2,7,9,3,1])
print(a)