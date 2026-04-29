# Problem: 20. Valid Parentheses
# Difficulty: Easy
# Explanation:
# Aqui lo que piden es validar si los parentesis/llaves/corchetes cierran bien.
# La idea es usar un stack: cada vez que vemos uno que abre, lo guardamos.
# Si vemos uno que cierra, verificamos si el ultimo que abrio es su pareja.
# Si en algun momento no cuadra, devolvemos False. Si al final el stack queda vacio,
# significa que todo cerro en orden y devolvemos True.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # Mapa de cierres -> su apertura correcta
        pares = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        # Stack para guardar los simbolos que abren
        stack = []

        # Recorremos la cadena caracter por caracter
        for ch in s:
            # Si abre, lo metemos al stack
            if ch in '([{':
                stack.append(ch)
            else:
                # Si cierra y no hay nada que comparar, ya es invalido
                if not stack:
                    return False

                # Sacamos el ultimo que abrio
                ultimo = stack.pop()

                # Si no hace pareja correcta, no sirve
                if ultimo != pares[ch]:
                    return False

        # Si queda algo en stack, faltaron cierres
        return len(stack) == 0
