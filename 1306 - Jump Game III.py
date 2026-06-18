from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        stack = deque([start])

        while stack:
            i = stack.popleft()

            if arr[i] == 0:
                return True
            if i in visited:
                continue
            
            visited.add(i)

            if i + arr[i] < len(arr):
                stack.append(i + arr[i])
            if 0 <= i - arr[i]:
                stack.append(i - arr[i])

        return False