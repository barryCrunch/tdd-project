import functools
import operator
from money import Money


class Portfolio:
    def __init__(self) -> None:
        self.moneys = []

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def evaluate(self, bank, currency):
        total = 0.0
        failures = []
        for m in self.moneys:
            try:
                total += bank.convert(m, currency).amount
            except Exception as ex:
                failures.append(ex)

        if len(failures) == 0:
            return Money(total, currency)

        failureMessage = ",".join(f.args[0] for f in failures)
        raise Exception("Missing exchange rate(s):[" + failureMessage + "]")

    def __convert(self, money, currency):
        exchangeRates = {"EUR->USD": 1.2, "USD->KRW": 1100}
        if money.currency == currency:
            return money.amount
        else:
            key = f"{money.currency}->{currency}"
            return money.amount * exchangeRates[key]
