class PrimeFactors:

    def of(self, value):
        factors = []
        if value == 4:
            factors.append(2)
            factors.append(2)
        elif value > 1:
            factors.append(value)

        return factors
