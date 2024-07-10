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
        factors = []
        divisor = 2

        if number > 1:
            while number % divisor != 0:
                divisor += 1
            factors.append(divisor)
            factors.extend(self.of_recursive(number // divisor))
        return factors
