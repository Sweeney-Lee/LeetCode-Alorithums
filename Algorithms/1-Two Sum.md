###### [Two Sum](https://leetcode.com/problems/two-sum/description/)
===
>	Given an array of integers, return indices of the two numbers such that they add up to a specific target.

>	You may assume that each input would have exactly one solution, and you may not use the same element twice.

>	Example:

>	Given nums = [2, 7, 11, 15], target = 9,

>	Because nums[0] + nums[1] = 2 + 7 = 9,
>	return [0, 1].
===
### Script:

#Mine:
    class Solution:
        def twoSum(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """
            length = len(nums)

            for i in range(length):
                for j in range(length-1,i, -1):
                    if nums[i] + nums[j] == target:
                        result = [i, j]
                        return result

            return []
                        
#Best:
    from collections import defaultdict

    class Solution:
        def twoSum( nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """
            nums_dict = defaultdict(list)
            for i in range(len(nums)):
                nums_dict[nums[i]].append(i)
            print(nums_dict)
            for i in range(len(nums)):
                other_num = target - nums[i]
                print(other_num)

                if other_num in nums_dict:
                    if other_num == nums[i]:
                        if len(nums_dict[other_num]) > 1:
                            return [i, nums_dict[other_num][-1]]
                    else:
                        return [i, nums_dict[other_num][0]]
