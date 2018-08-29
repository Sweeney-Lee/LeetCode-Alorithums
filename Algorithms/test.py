class Solution:
    def new21Game(self, N, K, W):

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
        he key recursion is f(x) = (1/W) * (f(x+1) + f(x+2) + ... + f(x+W))
        This is because there is a probability of \frac{1}{W} to draw each card from 1 to W
        """
s = Solution()
print(s.new21Game(N=10, K=1, W=10))
# print(s.new21Game(N=6, K=1, W=10))
# print(s.new21Game(N=21, K=17, W=10))
# print(s.new21Game(N = 0, K = 0, W = 1))