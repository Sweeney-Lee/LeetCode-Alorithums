#  **[Two Sum：](https://leetcode.com/problems/two-sum/description/)**

### *Description:*
>	Given an array of integers, return indices of the two numbers such that they add up to a specific target.

>	You may assume that each input would have exactly one solution, and you may not use the same element twice.

>	Example:

>	Given nums = [2, 7, 11, 15], target = 9,

>	Because nums[0] + nums[1] = 2 + 7 = 9,
>	return [0, 1].
---



### Script(Python):

#### Mine:
```
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
```
___

                        
#Best:
```
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
```
___
###### time: 6000ms VS ≈ 0ms
___

# conclude:
1. Use the defaultdict reverse the index and value

表头|表头|表头
---|:--:|---:
内容|内容|内容
内容|内容|内容


```flow 
st=>start: 注册印象笔记
e=>end: 您可以使用markdown
op1=>operation: 登录印象笔记
op2=>operation: 购买并登录马克飞象
cond=>condition: 是否已经购买并登录了马克飞象?

st->op1->cond
cond(yes)->e
cond(no)->op2->e
```
