# Problem: 21. Merge Two Sorted Lists
# Difficulty: Easy
# Explanation:
# Aqui nos dan dos listas enlazadas ya ordenadas y hay que unirlas en una sola,
# manteniendo el orden.
# La idea simple es comparar el nodo actual de cada lista y coger el menor.
# Ese nodo se pega al resultado y avanzamos en esa lista.
# Repetimos eso hasta que una lista se acabe, y luego pegamos lo que sobre.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Nodo dummy pa' arrancar facil sin enredarnos con casos especiales
        dummy = ListNode(0)

        # 'current' siempre apunta al final de la lista que vamos construyendo
        current = dummy

        # Mientras ambas listas tengan nodos, comparamos
        while list1 and list2:
            # Si list1 tiene el menor (o igual), lo pegamos
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                # Si no, pegamos el de list2
                current.next = list2
                list2 = list2.next

            # Avanzamos en la lista resultado
            current = current.next

        # Si sobro algo en list1 o list2, lo pegamos de una
        if list1:
            current.next = list1
        else:
            current.next = list2

        # El resultado real empieza despues del dummy
        return dummy.next
