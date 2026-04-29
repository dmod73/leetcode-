# Problem: 123. Best Time to Buy and Sell Stock III
# Difficulty: Hard
# Explanation:
# Aqui podemos hacer como maximo dos transacciones (comprar + vender).
# Vamos llevando 4 estados:
# 1) mejor costo despues de la primera compra
# 2) mejor ganancia despues de la primera venta
# 3) mejor costo despues de la segunda compra (usando ganancia de la primera)
# 4) mejor ganancia despues de la segunda venta
# Al final, la mejor respuesta es la ganancia de la segunda venta.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # No hay dias, no hay ganancia
        if not prices:
            return 0

        # Estados iniciales
        buy1 = float('inf')
        sell1 = 0
        buy2 = float('inf')
        sell2 = 0

        # Recorremos cada precio una sola vez
        for price in prices:
            # Mejor primera compra (queremos pagar lo menos posible)
            if price < buy1:
                buy1 = price

            # Mejor primera venta
            if price - buy1 > sell1:
                sell1 = price - buy1

            # Mejor segunda compra (precio real descontando primera ganancia)
            if price - sell1 < buy2:
                buy2 = price - sell1

            # Mejor segunda venta
            if price - buy2 > sell2:
                sell2 = price - buy2

        return sell2
