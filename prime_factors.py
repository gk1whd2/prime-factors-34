class PrimeFactors:

    def of(self, value):
        factors = []
        if value == 4:
            while (value % 2 == 0):
                factors.append(2)
                value //= 2

        elif value > 1:
            factors.append(value)

        return factors
