
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ph_list = [[],[],['a', 'b', 'c'], ['d', 'e', 'f'],['g','h','i'],['j','k','l'], 
                   ['m','n','o'],['p', 'q', 'r', 's'],['t','u','v'],['w','x','y','z']]
        dig_len = len(digits)
        result_len = 1
        for i in digits:
            result_len *= (4 if i == 9 or i == 7 else 3)
        
        result = ['' for i in range(result_len)]
        for i in range(result_len):
            x = i
            # print(str(i) + ':')
            for j in range(dig_len):
                if j == 0:
                    m = x % (4 if digits[0] == '9' or digits[0] == '7' else 3)
                    # print(x)
                    result[i] += ph_list[int(digits[j])][m]
                else :
                    x = x // (4 if digits[j] == '9' or digits[j] == '7' else 3)
                    # print(x)
                    result[i] += ph_list[int(digits[j])][x]  
                print(result)
        return result
s = Solution()
a = s.letterCombinations('234')
print(a)
