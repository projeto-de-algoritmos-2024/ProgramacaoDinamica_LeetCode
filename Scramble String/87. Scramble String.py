class Solution:
  @functools.lru_cache(None)  # Utiliza cache para armazenar os resultados das chamadas recursivas, otimizando a execução.
  def isScramble(self, s1: str, s2: str) -> bool:
    # Verifica se as duas strings são iguais.
    if s1 == s2:
      return True
    
    # Verifica se as duas strings possuem a mesma contagem de caracteres, caso contrário, não pode ser uma "scramble".
    if collections.Counter(s1) != collections.Counter(s2):
      return False

    # Para cada posição i, verifica as duas possibilidades de divisão das strings.
    for i in range(1, len(s1)):
      # Primeiro caso: verifica se as duas primeiras partes e as duas últimas partes das strings correspondem.
      if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
        return True

      # Segundo caso: verifica se a primeira parte de s1 corresponde à última parte de s2, e a última parte de s1 à primeira parte de s2.
      if (self.isScramble(s1[:i], s2[len(s2) - i:]) and
              self.isScramble(s1[i:], s2[: len(s2) - i])):
        return True

    # Se nenhum dos casos anteriores se aplicar, retorna False, indicando que s1 não pode ser uma versão embaralhada de s2.
    return False