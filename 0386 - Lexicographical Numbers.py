class Solution:
    # SORT SOLUTION
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        for i in range(1, n+1):
            res.append(i)

        res.sort(key=str)

        return res

    # DFS SOLUTION
    def lexicalOrder2(self, n: int) -> List[int]:
        res = []

        def dfs(cur):
            if cur > n:
                return
            res.append(cur)
            cur *= 10

            for i in range(10):
                dfs(cur + i)
            
        for i in range(1, 10):
            dfs(i)
        
        return res