# approach:
# Use DFS to spread rot recursively from each rotten orange
# Update each fresh orange with the minimum time it took to rot it
# At the end, find the maximum time used to rot all fresh oranges

# #TC: O(m * n) - Every cell is visited at most once.
# #SC: O(m * n) - Stack space in worst case for DFS recursion.

from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(x, y, time):
            # Boundary checks
            if x < 0 or x >= rows or y < 0 or y >= cols:
                return
            # If cell is empty or has a rotten orange with earlier time, skip
            if grid[x][y] == 0 or (grid[x][y] > 1 and grid[x][y] < time):
                return

            grid[x][y] = time
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(x + dx, y + dy, time + 1)

        # Run DFS from all initially rotten oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    dfs(r, c, 2)  # Start time from 2 to differentiate from fresh 1s

        max_time = 2
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:  # Unreachable fresh orange
                    return -1
                max_time = max(max_time, grid[r][c])

        return max_time - 2  # Subtract offset


if __name__ == "__main__":
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    sol = Solution()
    print("Minutes to rot all oranges (DFS):", sol.orangesRotting(grid))
