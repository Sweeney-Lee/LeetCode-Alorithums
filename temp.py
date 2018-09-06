class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def upper_bound(alist, start, end, key):
            if alist[end] <= key:
                return end + 1
            while start < end:
                mid = start + (end - start) // 2
                if alist[mid] <= key:
                    start = mid + 1
                else:
                    end = mid
            return start

        LIS = [0 for i in range(len(nums))]
        LIS[0] = nums[0]
        length = 1
        for i in range(len(nums)):
            pos = upper_bound(LIS, 0, length - 1, nums[i])
            LIS[pos] = nums[i]
            if pos + 1 > length:
                length = pos + 1
        return length

s = Solution()
a = s.lengthOfLIS([2,2])
print (a)

