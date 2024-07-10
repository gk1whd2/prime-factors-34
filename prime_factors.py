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
        if number == 2:
            factors = [2]
        if number == 3:
            factors = [3]

        if number == 4:
            if number % 2 == 0:
                factors.append(2)
                factors.extend(self.of_recursive(number // 2))
                number //= 2
        if number == 6:
            if number % 2 == 0:
                factors.append(2)
                factors.extend(self.of_recursive(number // 2))
                number //= 2
        return factors
