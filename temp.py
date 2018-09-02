class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        length = len(nums)

        num_0 = []
        for i in range(length):
            if nums[i] == 0:
                num_0.append(i)
                break
        if len(num_0) >= 3:
            # C len(num_0) 3

            result.append([0,0,0] * )
        if negative == 0 or negative == len(nums) - 1 or negative == None:
            return []
        result = []
        negative = num_0[0]
        for i in range(0, negative + 1):
            for j in range(negative + 1, length):
                if (nums[i] + nums[j]) >= 0:
                    for k in range(i + 1, negative + 1):
                        sum = nums[i] + nums[j] + nums[k]
                        if sum == 0:
                            result.append([nums[i], nums[k], nums[j]])
                        if sum < 0:
                            break

                else:
                    for k in range(j + 1, length):
                        sum = nums[i] + nums[j] + nums[k]
                        if sum == 0:
                            result.append([nums[i], nums[k], nums[j]])
                        if sum > 0:
                            break
        return result