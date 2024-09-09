class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # inicializar a matriz
        pd = [[0] * (n + 1) for _ in range(m + 1)]
        
        # caso base
        for i in range(m + 1):
            pd[i][0] = 1  # tem uma maneira de corresponder um t vazio com qualquer s
        for j in range(1, n + 1):
            pd[0][j] = 0  # não tem maneira de corresponder um t não vazio com um s vazio
        
        # preenche a matriz
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    pd[i][j] = pd[i - 1][j - 1] + pd[i - 1][j]
                else:
                    pd[i][j] = pd[i - 1][j]
        
        return pd[m][n]
