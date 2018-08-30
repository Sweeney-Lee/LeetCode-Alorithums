
#  **[7. Reverse Integer：](https://leetcode.com/problems/reverse-integer/)**

### *Description:*

    Given a 32-bit signed integer, reverse digits of an integer.

    Example 1:

    Input: 123
    Output: 321
    Example 2:

    Input: -123
    Output: -321
    Example 3:

    Input: 120
    Output: 21
    Note:
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

---

### Script `Python` :

> Mine:
```

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        fu = False
        if x < 0:
            fu = True
            x = -(x)
            
        st = str(x)
        st1 = st[::-1]
        result = int(st1)
        
        if result >> 31 != 0 :
            result =  0
        if fu:
            result = - result
        return result


```
___

                        
> Best:
```
   
   As Mine

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
    <th>52</th>
    <th>~</th>
<table>

___

# conclude:
1. use the technique : list[::-1] to reverse
2. change int to string 
3. use the Bit manipulation to compare number




        
