
import functools
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ph_list = [[],[],['a', 'b', 'c'], ['d', 'e', 'f'],['g','h','i'],['j','k','l'], 
                   ['m','n','o'],['p', 'q', 'r', 's'],['t','u','v'],['w','x','y','z']]
        key_list = [0,0,3,3,3,3,3,4,3,3,] 
        change_list = [key_list[int(i)] for i in digits]
        change_list.append(1)
        print(change_list)
        dig_len = len(digits)
        result_len = 1
        product = lambda x, y: x * y
        for i in digits:
            result_len *= key_list[i]
        
        result = ['' for i in range(result_len)]
        for i in range(result_len):
            # print(str(i) + ':')
            for j in range(dig_len):
                a = functools.reduce(product, change_list[j - 1])
                b = functools.reduce(product, change_list[j - 1])
                x = i % change_list[j]
                result[i] += ph_list[int(digits[j])][x]  
                print(result)
        return result

# alist = functools.reduce(lambda x, y: x + y, [1, 3, 5, 7, 9])
# print(alist)
s = Solution()
a = s.letterCombinations('2743')
print(a)

s = Solution()
a = s.letterCombinations('234')
print(a)
