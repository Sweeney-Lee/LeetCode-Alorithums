class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        len_s, len_p = len(s), len(p)
        if len_s == 0 and (len_p == 0 or (len_p == 1 and p == '.') or (len_p == 2 and p[1] == '*')):
          return True
        if len_p == 0:
          return False
        # p1, p2 == 0
        return subIsMatch(0, 0)
        def subIsMatch(p1, p2):
          while p1 < len_s and p2 < len_p:
            if s[p1] == p[p2] or p[p2] == '.':
              p1, p2 = p1 + 1, p2 + 1
            elif p[p2] == '*':
              if s[p1] == p[p2 - 1]:
                p1 = p1 + 1
              elif p[p2 - 1] != '.':
                p2 = p2 + 1
              # .*
              else:
                if p2 == len_p - 1:
                  return True
                else:
                  value =  p[p2 + 1]
                  index = s.find(value, p1)
                  while 
            else:
              return False
          return True

s = Solution()
a = s.isMatch("mississippi", "mis*is*p*.")
print(a)