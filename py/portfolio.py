import functools
import operator
from money import Money


class Portfolio:
    def __init__(self) -> None:
        self.moneys = []

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def evaluate(self, currency):
        total = functools.reduce(
            operator.add, map(lambda m: self.__convert(m, currency), self.moneys), 0
        )
        return Money(total, currency)

    def __convert(self, money, currency):
        exchangeRates = {"EUR->USD": 1.2, "USD->KRW": 1100}
        if money.currency == currency:
            return money.amount
        else:
            key = f"{money.currency}->{currency}"
            return money.amount * exchangeRates[key]
