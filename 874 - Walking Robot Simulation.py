class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [[0,1], [1,0], [0,-1],[-1,0]]
        d = 0
        x, y = 0, 0
        dist = 0
        obstacles = {tuple(o) for o in obstacles}

        print(obstacles)

        for c in commands:
            if c == -1:
                d = (d + 1) % 4
            elif c == -2:
                d = (d - 1) % 4
            else:
                for _ in range(c):
                    if (x + directions[d][0], y + directions[d][1]) in obstacles:
                        break
                    x += directions[d][0]
                    y += directions[d][1]

            dist = max(dist, x**2 + y**2)

        return dist