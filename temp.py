class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        a = [s[0]]
        i = 1
        while i < len(s):
            if s[i] in ['(', '{', '[']:
                a.append(s[i])
            elif len(a) >= 1 and ((s[i] == ')' and a[-1] == '(') or (s[i] == '}' and a[-1] == '{') or (s[i] == ']' and a[-1] == '[')):
                    a.pop()
            else:
                return False
            i += 1
        return True
s = Solution()
a = s.isValid("{}][}}{[))){}{}){(}]))})[({")
print(a)
