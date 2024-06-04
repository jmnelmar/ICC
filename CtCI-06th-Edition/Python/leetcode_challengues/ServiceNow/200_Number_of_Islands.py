import collections
def numIslands(self, grid: [[str]]) -> int:
    m, n = len(grid), len(grid[0])
    num_islands = 0

    def dfs(pos):
        i, j = pos
        directions = [ (0, 1), (1, 0), (-1, 0), (0,-1)]
        for i_off, j_off in directions:
            r, c = i + i_off, j+j_off
            if r >= 0  and r < m and c >= 0 and c < n and grid[r][c] == '1':
                grid[r][c] = '2'
                dfs((r,c))
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                num_islands += 1
                grid[i][j] = '2'
                dfs((i,j))

    return num_islands
            