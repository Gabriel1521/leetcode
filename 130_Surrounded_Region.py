class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        queue = collections.deque([])
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i in [0,len(board)-1] or j in [0,len(board[0])-1]) and board[i][j] == 'O':
                    queue.append([i,j])

        while queue:
            x, y = queue.popleft()
            if 0<=x<len(board) and 0<=y<len(board[0]) and board[x][y] == 'O':
                board[x][y] = 'D'
                queue.append([x-1,y])
                queue.append([x+1,y])
                queue.append([x,y-1])
                queue.append([x,y+1])

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'D':
                    board[i][j] = 'O'

        return board
