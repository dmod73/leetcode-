# Problem: 9. Palindrome Number
# Difficulty: Easy
# Explanation:
# Un palindrome es un numero que se lee igual pa' alante y pa' atras.
# Aqui usamos la forma mas simple: convertimos el numero a string,
# viramos el string, y comparamos ambos.
# Si son iguales, devolvemos True; si no, False.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # Paso 1: Pasar el entero a texto
        original = str(x)

        # Paso 2: Virar el texto
        invertido = original[::-1]

        # Paso 3: Comparar y devolver el resultado
        return original == invertido
