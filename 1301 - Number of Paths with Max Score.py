class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        mod = 10**9 + 7
        rows = len(board)
        cols = len(board[0])

        dp = [[[-1, 0] for _ in range(cols)] for _ in range(rows)]
        dp[-1][-1] = [0, 1]
        
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if board[r][c] == 'X': continue
                val = 0 if board[r][c] in 'SE' else int(board[r][c])
                best, count = -1, 0

                for nr, nc in ((r+1, c), (r, c+1), (r+1, c+1)):
                    if nr >= rows or nc >= cols: continue
                    score, ncount = dp[nr][nc]
                    if score < 0: continue
                    
                    if score > best:
                        best, count = score, ncount
                    elif score == best:
                        count = (count + ncount) % mod

                if best != -1:
                    dp[r][c] = [best + val, count]
                    
        return dp[0][0] if dp[0][0][0] != -1 else [0, 0]
