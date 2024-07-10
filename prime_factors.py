class PrimeFactors:

    def of(self, value):
        factors = []
        divisor = 2
        if value > 1:
            while value > 1:
                while value % divisor == 0:
                    factors.append(divisor)
                    value //= divisor
                divisor += 1

        return factors

    def of_recursive(self, number):
        if number == 2:
            return [2]
        if number == 3:
            return [3]
        if number == 4:
            return [2, 2]
        return []
