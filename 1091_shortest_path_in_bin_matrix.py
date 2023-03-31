class Solution:
    def shortestPathBinaryMatrix(self, grid):
        h = len(grid)
        w = len(grid[0])
        short_path = float("inf")
        for r in reversed(range(h)):
            for c in reversed(range(w)):
                if grid[r][c] ==1:
                    grid[r][c] ="x"
        
        
        for r in reversed(range(h)):
            for c in reversed(range(w)):
                directions = [(r,c+1),(r+1,c+1),(r+1,c),(r+1,c-1),(r,c-1),(r-1,c-1),(r-1,c),(r-1,c+1)]
                if grid[r][c] ==0:
                    if r == h-1 and c== w-1:
                        grid[r][c] = 1
                    else:
                        paths = []
                        for (r1,c1) in directions:
                            if 0 <=r1 < h and 0 <=c1 < w and grid[r1][c1] != "x" and grid[r1][c1] != "0":
                                 paths.append(grid[r1][c1])
                        grid[r][c] = min(paths)+1
        
        
        return grid[0][0]
                    
        



grid = [[0,0,0],[1,1,0],[1,1,0]]
obj = Solution()
print(obj.shortestPathBinaryMatrix(grid)) 


[[0,1,1,0,0,0],
 [0,1,0,1,1,0],
 [0,1,1,0,1,0],
 [0,0,0,1,1,0],
 [1,1,1,1,1,0],
 [1,1,1,1,1,0]]