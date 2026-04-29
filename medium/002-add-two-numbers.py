# Problem: 2. Add Two Numbers
# Difficulty: Medium
# Explanation:
# Aqui cada lista enlazada representa un numero, pero al reves.
# Tenemos que sumar ambos numeros y devolver otra lista enlazada tambien al reves.
# La forma mas directa es sumar digito por digito, igual que en papel,
# guardando el carry (acarreo) cuando la suma pasa de 9.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Nodo dummy pa' construir la lista resultado sin complicarnos
        dummy = ListNode(0)
        current = dummy

        # Acarreo de la suma (cuando pasa de 9)
        carry = 0

        # Seguimos mientras haya nodos en l1 o l2, o quede carry
        while l1 or l2 or carry:
            # Valor actual de cada lista (si no hay nodo, vale 0)
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Suma total del digito actual
            total = v1 + v2 + carry

            # Nuevo digito y nuevo carry
            digit = total % 10
            carry = total // 10

            # Pegamos el digito al resultado
            current.next = ListNode(digit)
            current = current.next

            # Avanzamos en l1 y l2 si todavia tienen nodos
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # El resultado real empieza despues del dummy
        return dummy.next
