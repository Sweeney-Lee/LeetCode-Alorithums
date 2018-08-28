
#  **[ ***：](https://***)**

### *Description:*
> 1
> 2
> 3
---


### Script `Python` :

#### Mine:
```

***

```
___

                        
#### Best:
```
   
   ***

```
___
 

  VS    |  Mine   |  Best
  ---   |  :--:   |  ---:
time(ms)|    /    |   /
space   |    /    |   / 

___

# conclude:
1. ***


---
class Solution:
    
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        def judge_N(x):
            if x > N:
                return 0
            else:
                return 1
        if K == 0:
            return 1
        Max = K - 1 + W
        alist = {}
        for i in range(1, Max + 1):
            alist[i] = 0
        result = 0
        for i in range(Max, 0, -1):
            if i >= K:
                alist[i] = judge_N(i)
            else:
                for m in range(1, W + 1):
                    alist[i] += alist[i + m] / W
        for i in range(1, W + 1):
            result += alist[i] /W
        return result
        
