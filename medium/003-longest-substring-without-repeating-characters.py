# Problem: 3. Longest Substring Without Repeating Characters
# Difficulty: Medium
# Explanation:
# Aqui hay que sacar el largo del pedazo mas largo de texto (substring)
# que no repita caracteres.
# Usamos una ventana deslizante con dos punteros.
# Si un caracter se repite dentro de la ventana actual,
# movemos el inicio pa' despues de donde se vio ese caracter por ultima vez.
# Asi siempre mantenemos una ventana valida sin repetidos.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Guarda la ultima posicion donde vimos cada caracter
        ultima_pos = {}

        # Inicio de la ventana actual
        inicio = 0

        # Mejor largo encontrado
        mejor = 0

        # Recorremos cada caracter con su indice
        for i, ch in enumerate(s):
            # Si el caracter ya estaba dentro de la ventana,
            # movemos el inicio justo despues de su posicion anterior
            if ch in ultima_pos and ultima_pos[ch] >= inicio:
                inicio = ultima_pos[ch] + 1

            # Guardamos/actualizamos la ultima posicion del caracter
            ultima_pos[ch] = i

            # Largo de la ventana actual
            largo_actual = i - inicio + 1

            # Actualizamos el mejor largo si mejoro
            if largo_actual > mejor:
                mejor = largo_actual

        return mejor
