from collections import defaultdict
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        # 去除[1, 2] 和 [1, 2], [-1, -2]
        if len(nums) < 3 or nums[0] > 0 or nums[-1] < 0:
            return []
            
        length = len(nums)
        mid = None
        num_0 = []
        result = []
        def equal(a,b):
            if a[0] == b[0] and a[1] == b[1] and a[2] == b[2]:
                return True
            return False
        
        # 计算0个数和位置，如果没有0，记录中间位置
        for i in range(length):
            if nums[i] == 0:
                num_0.append(i)
            if nums[-1] != 0 and nums[i] <= 0 and nums[i + 1] > 0:
                mid = i
        len_num_0 = len(num_0)

        if len_num_0 >= 1:
            if len_num_0 >= 3:
                result.append([0,0,0])
            if nums[0] == 0 or nums[-1] == 0:
                if len_num_0 >= 3:
                    return result
                else:
                    return []
            left_0, right_0 = num_0[0], num_0[-1]
        else:
            left_0, right_0 = mid, mid
            
        for i in range(0, left_0 + 1):
            for j in range(length - 1,right_0, -1):
                if (nums[i] + nums[j]) > 0:
                    for k in range(i + 1, left_0 + 1):
                        sum = nums[i] + nums[j] + nums[k]
                        if sum == 0:
                            result.append([nums[i], nums[k], nums[j]])
                            break
                        if sum > 0:
                            break

                elif (nums[i] + nums[j]) < 0:
                    for k in range(j - 1, right_0, -1):
                        sum = nums[i] + nums[j] + nums[k]
                        if sum == 0:
                            result.append([nums[i], nums[j], nums[k]])
                            break
                        if sum < 0:
                            break
                else:
                    if len(num_0) >=1:
                        result.append([nums[i],0, nums[j]]) 
        if len(result) == 1:
            return result
        else:
            nums_dict = defaultdict(list)
            for i in range(len(result)):
                nums_dict[''.join(str(e) for e in result[i])].append(result[i])
        result = []
        for i in nums_dict.keys():
            result.append(nums_dict[i][0])
        return result