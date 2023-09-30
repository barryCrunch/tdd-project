from money import Money


class Bank:
    def __init__(self, exchangeRates=None) -> None:
        self.exchangeRates = exchangeRates or {}

    def addExchangeRate(self, currencyFrom, currencyTo, rate):
        key = f"{currencyFrom}->{currencyTo}"
        self.exchangeRates[key] = rate

    def convert(self, aMoney, aCurrency):
        if aMoney.currency == aCurrency:
            return Money(aMoney.amount, aCurrency)

        key = f"{aMoney.currency}->{aCurrency}"
        if key in self.exchangeRates:
            return Money(aMoney.amount * self.exchangeRates[key], aCurrency)

        raise Exception(key)
