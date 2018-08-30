
#  **[ 837.New 21 Game：](https://leetcode.com/problems/new-21-game/description/)**

### *Description:*
    Alice plays the following game, loosely based on the card game "21".

    Alice starts with 0 points, and draws numbers while she has less than K points.  During each draw, she gains an integer number of points randomly from the range [1, W], where W is an integer.  Each draw is independent and the outcomes have equal probabilities.

    Alice stops drawing numbers when she gets K or more points.  What is the probability that she has N or less points?

    Example 1:

    Input: N = 10, K = 1, W = 10
    Output: 1.00000
    Explanation:  Alice gets a single card, then stops.
    Example 2:

    Input: N = 6, K = 1, W = 10
    Output: 0.60000
    Explanation:  Alice gets a single card, then stops.
    In 6 out of W = 10 possibilities, she is at or below N = 6 points.
    Example 3:

    Input: N = 21, K = 17, W = 10
    Output: 0.73278
    Note:

    0 <= K <= N <= 10000
    1 <= W <= 10000
    Answers will be accepted as correct if they are within 10^-5 of the correct answer.
    The judging time limit has been reduced for this question.
---


### Script `Python` :

> Mine:
```

class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        if K == 0:
            return 1
        dp = [0.0] * (K + W )
        sum = [0.0] * (K + W + 1)
        for i in range(K + W -1, -1, -1):
            if i > N: continue
            if i >= K:
                dp[i] = 1.0
            else:
                dp[i] = (sum[i + 1] - sum[i + 1 + W]) / W

            sum[i] = sum[i + 1] + dp[i]
        return dp[0]

```
___

                        
> Best:
```
   
class Solution:
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        dp = [0.0] * (N + W + 1)
        # dp[x] = the answer when Alice has x points
        for k in range(K, N + 1):
            dp[k] = 1.0

        S = min(N - K + 1, W)
        # S = dp[k+1] + dp[k+2] + ... + dp[k+W]
        for k in range(K - 1, -1, -1):
            dp[k] = S / W
            S += dp[k] - dp[k + W]

        return dp[0]
    
        """
        he key recursion is f(x) = (1/W) * (f(x+1) + f(x+2) + ... + f(x+W))This is because there is a probability of \frac{1}{W} to draw each card from 1 to W
        """

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
    <th>136</th>
    <th>80</th>
<table>

___

# conclude:
1. change d[x + 1] + d[x + 2] + ...d[x + W] to d[X] - d[W]
2. add the N in params to avoid judge  



