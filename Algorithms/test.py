# class Solution:
#
#     def new21Game( N, K, W):
#
#         if K == 0:
#             return 1
#
#         Max = K - 1 + W
#         alist = {}
#         result = 0
#         for i in range(Max, 0, -1):
#             alist[i] = 0
#             if i >= K:
#                 if i > N:
#                     alist[i] = 1
#             else:
#                 for m in range(1, W + 1):
#                     alist[i] += alist[i + m] / W
#         for i in range(1, W + 1):
#             result += alist[i] /W
#         return 1- result
import functools
class Solution:

    def new21Game(N, K, W):
        if K == 0:
            return 1

        def get_Sum(alist):
            result = 0
            for i in alist:
                result += alist[i] / W
            return result
        alist = [[0] for i in range(K+W  + 1)]
        result = 0

        for i in range(K , K+W  + 1):
            alist[i] = 0 if i > N else 1

        for i in range(K + 1):

            first = get_Sum(alist)
            alist.insert(0, first)
            alist.pop()

        result = get_Sum(alist)
        return 1 - result

a = Solution.new21Game(21,17,10)
print(a)

# li = [1, 2, 3, 4, 5]
# a = 3
# A = functools.reduce(lambda x, y, a: x * y + a , a, li)
# print(A)
# K = 3
# W = 3
# alist = [[0] for i in range(K + W + 1)]
# print(alist)