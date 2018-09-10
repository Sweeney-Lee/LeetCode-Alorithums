class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def nextS(wordList, i, j):
            blist = [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]
            return [x for x in blist if x not in wordList and (0 <= x[0] < len(board)) and (0 <= x[1] < len(board[0])) ]
            

        def judgeA(i, j, index, alist):
            if index == len(word) - 1: 
                self.result = True                
                return True
            index += 1
            for m in nextS(alist, i, j):
                print(board[m[0]][m[1]])
                if board[m[0]][m[1]] == word[index]:
                    alist.append((i,j))
                    print(index)
                    judgeA(m[0], m[1], index + 1, alist)
                
        self.result = False
        
        lenWord = len(word)
        lenBoard = len(board) * len(board[0])
        if lenWord > lenBoard: return False
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    judgeA(i, j, 0, [[i, j]])
                    if self.result: return True
                    
        return False
s = Solution()
a = s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
# a = s.exist([["a","a"]], "a")
print(a)