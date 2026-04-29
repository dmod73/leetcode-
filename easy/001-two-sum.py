# Problem: 1. Two Sum
# Difficulty: Easy
# Explanation:
# Aqui buscamos dos posiciones del arreglo que sumen el target.
# Lo hacemos en una sola pasada usando un diccionario (numero -> indice).
# Por cada numero, calculamos el complemento que falta pa' llegar al target.
# Si ese complemento ya salio antes, devolvemos los dos indices y ya.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Guardamos lo que ya vimos: numero -> indice
        vistos = {}

        # Recorremos el arreglo con indice y valor
        for i, num in enumerate(nums):
            # Numero que falta para completar el target
            complemento = target - num

            # Si ya estaba, encontramos la contestacion
            if complemento in vistos:
                return [vistos[complemento], i]

            # Si no estaba, guardamos el numero actual
            vistos[num] = i
