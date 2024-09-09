class Solution:
  def isMatch(self, s: str, p: str) -> bool:
    m = len(s)  
    n = len(p)  
    

    # dp é uma matriz de booleanos onde dp[i][j] indica se os primeiros 'i' caracteres de 's'
    # correspondem aos primeiros 'j' caracteres de 'p'.
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True  

    # verificar se s[i] corresponde a p[j].
    # Se p[j] for '.', ele corresponde a qualquer caractere de s[i].
    def isMatch(i: int, j: int) -> bool:
      return j >= 0 and (p[j] == '.' or s[i] == p[j])

    #  se o padrão começar com '*' (na posição j), ele pode corresponder à string vazia.
    for j, c in enumerate(p):
      if c == '*' and dp[0][j - 1]:
        dp[0][j + 1] = True  # Um '*' pode fazer o padrão corresponder a uma string vazia.

    # Preenchendo a tabela dp com base nas comparações entre a string 's' e o padrão 'p'.
    for i in range(m):
      for j in range(n):
        if p[j] == '*':  # Se o caractere no padrão for '*':
          # 'noRepeat' verifica se ignoramos o '*' (como se ele não estivesse lá).
          noRepeat = dp[i + 1][j - 1]
          # 'doRepeat' verifica se podemos repetir o caractere anterior ao '*' para corresponder a s[i].
          doRepeat = isMatch(i, j - 1) and dp[i][j + 1]
          # A posição dp[i + 1][j + 1] é verdadeira se uma dessas duas possibilidades funcionar.
          dp[i + 1][j + 1] = noRepeat or doRepeat
        elif isMatch(i, j):  # Se o caractere s[i] corresponder a p[j]:
          dp[i + 1][j + 1] = dp[i][j]  # Avançamos tanto no padrão quanto na string.

    return dp[m][n]  # O resultado final está em dp[m][n], que indica se a string 's' corresponde a 'p'.