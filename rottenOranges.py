# #approach:
# Perform (4-directional) BFS from all initially rotten oranges
# At each minute (each BFS level), rot adjacent fresh orange
# Continue until no fresh orange remains or no progress can be made

# #TC: O(m * n) - Each cell is processed at most once in the worst case
# #SC: O(m * n) - Queue can hold all cells in the worst case (all rotten)

from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if rows == 0:
            return -1

        cols = len(grid[0])
        fresh_cnt = 0
        rotten = deque()

        # Count fresh oranges and track rotten oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh_cnt += 1

        minutes_passed = 0

        # BFS to rot adjacent fresh oranges
        while rotten and fresh_cnt > 0:
            minutes_passed += 1
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    xx, yy = x + dx, y + dy
                    if xx < 0 or xx == rows or yy < 0 or yy == cols:
                        continue
                    if grid[xx][yy] != 1:
                        continue

                    fresh_cnt -= 1
                    grid[xx][yy] = 2
                    rotten.append((xx, yy))

        return minutes_passed if fresh_cnt == 0 else -1


if __name__ == "__main__":
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    sol = Solution()
    print("Minutes to rot all oranges:", sol.orangesRotting(grid))
