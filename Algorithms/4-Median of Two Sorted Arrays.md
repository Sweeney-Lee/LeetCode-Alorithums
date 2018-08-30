
#  **[4. Median of Two Sorted Arrays:](https://leetcode.com/problems/median-of-two-sorted-arrays/description/)**

### *Description:*
    There are two sorted arrays nums1 and nums2 of size m and n respectively.

    Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

    You may assume nums1 and nums2 cannot be both empty.

    Example 1:

    nums1 = [1, 3]
    nums2 = [2]

    The median is 2.0
    Example 2:

    nums1 = [1, 2]
    nums2 = [3, 4]

    The median is (2 + 3)/2 = 2.5

---


### Script `Python` :

> Mine:
```

import math
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = nums1 + nums2
        num.sort()
        length = len(num)
        mid = int(math.floor(length / 2))

        if length & 1 == 0 :
            median = (num[mid] + num[mid - 1])/2
        else: 
            median = num[mid]
        return median

```
___

                        
> Best:
```
   
   As Me

```
___
 

<table>
  <tr>
    <th>VS</th>
    <th>Mine</th>
    <th>Best</th>
  </tr>
    <tr>
    <th>time(ms)</th>
    <th>92</th>
    <th>~</th>
  </tr>
    <tr>
    <th>space</th>
    <th>/</th>
    <th>/</th>
  </tr>
<table>

___

# conclude:
1. use math.floor() or //




        
