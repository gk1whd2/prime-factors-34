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
        dividor = 2

        if number == 2:
            factors = [2]
        if number == 3:
            factors = [3]

        if number > 3:
            if number % dividor == 0:
                factors.append(dividor)
                factors.extend(self.of_recursive(number // dividor))
                number //= dividor
        return factors
