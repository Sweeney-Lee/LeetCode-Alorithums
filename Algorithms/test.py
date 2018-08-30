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
