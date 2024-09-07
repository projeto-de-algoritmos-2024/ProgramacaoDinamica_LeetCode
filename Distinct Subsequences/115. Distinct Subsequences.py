class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # caso base
        for i in range(m + 1):
            dp[i][0] = 1  # tem uma maneira de corresponder um t vazio com qualquer s
        for j in range(1, n + 1):
            dp[0][j] = 0  # não tem maneira de corresponder 
