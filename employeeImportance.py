# approach:
# Create a hashmap to map employee ID to the Employee object.
# DFS: Recursively add importance of current employee and all subordinates.
# BFS: Use a queue to traverse level by level, summing up importance values.

# TC: O(n) - Each employee is visited once.
# SC: O(n) - Hashmap + recursion stack or queue space.

from typing import List
from collections import deque


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    # DFS Approach
    def getImportanceDFS(self, employees: List[Employee], id: int) -> int:
        emp_map = {e.id: e for e in employees}

        def dfs(emp_id):
            emp = emp_map[emp_id]
            total = emp.importance
            for sub_id in emp.subordinates:
                total += dfs(sub_id)
            return total

        return dfs(id)

    # BFS Approach
    def getImportanceBFS(self, employees: List[Employee], id: int) -> int:
        emp_map = {e.id: e for e in employees}
        total = 0
        queue = deque([id])

        while queue:
            curr_id = queue.popleft()
            emp = emp_map[curr_id]
            total += emp.importance
            queue.extend(emp.subordinates)

        return total


if __name__ == "__main__":

    employees = [Employee(1, 5, [2, 3]), Employee(2, 3, []), Employee(3, 3, [])]

    sol = Solution()

    print("DFS Total Importance:", sol.getImportanceDFS(employees, 1))
    print("BFS Total Importance:", sol.getImportanceBFS(employees, 1))
