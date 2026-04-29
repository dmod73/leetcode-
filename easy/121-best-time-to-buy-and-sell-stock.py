# Problem: 121. Best Time to Buy and Sell Stock
# Difficulty: Easy
# Explanation:
# Aqui queremos sacar la ganancia maxima comprando una vez y vendiendo despues.
# Recorremos los precios una sola vez.
# Vamos guardando el precio mas bajito visto hasta ahora (mejor dia pa' comprar)
# y en cada dia calculamos cuanto ganariamos si vendemos ahi.
# Si esa ganancia es mejor que la anterior, la actualizamos.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # Si no hay precios, no hay forma de ganar
        if not prices:
            return 0

        # Precio minimo visto hasta el momento (dia de compra ideal por ahora)
        min_price = prices[0]

        # Mejor ganancia encontrada
        max_profit = 0

        # Recorremos cada precio
        for price in prices:
            # Si encontramos un precio mas bajo, actualizamos compra
            if price < min_price:
                min_price = price

            # Ganancia si compro en min_price y vendo hoy
            profit_today = price - min_price

            # Si mejora la ganancia maxima, la guardamos
            if profit_today > max_profit:
                max_profit = profit_today

        # Si nunca hubo ganancia positiva, se queda en 0
        return max_profit
