class Solution:
    def solve( board):
        """
        Do not return anything, modify board in-place instead.
        """
        
        h = len(board)
        w = len(board[0])
        
        free_zeros = []
        marginal_zeros = []
        
        for r in range(h):
            if board[r][0] == "O":
                marginal_zeros.append((r,0))
            if board[r][w-1] == "O":
                marginal_zeros.append((r,w-1))
        
        
        for c in range(1,w-1):
            if board[0][c] == "O":
                marginal_zeros.append((0,c))
            if board[h-1][c] == "O":
                marginal_zeros.append((h-1,c) )   
        
        def capture(r,c):
            if (r,c) not in free_zeros:
                free_zeros.append((r,c))
                directions = [(r,c+1),(r+1,c),(r,c-1),(r-1,c)]
                for r1,c1 in directions:
                    if 0 <=r1 < h and 0 <=c1 < w and board[r1][c1] == "O" and (r1,c1) not in free_zeros:                
                        capture(r1,c1)
        
        for r,c in marginal_zeros:
            capture(r,c)
            
        for r in range(h):
            for c in range(w):
                if board[r][c] == "O" and (r,c) not in free_zeros:
                    board[r][c] = "X"        
        return board


board = [["O","O","O"],
         ["O","O","O"],
         ["O","O","O"]] 
obj = Solution()
print(Solution.solve(board))



["X","X","X","X"],
["X","O","O","X"],
["X","X","O","X"],
["X","O","X","X"]