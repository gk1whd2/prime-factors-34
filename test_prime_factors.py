from unittest import TestCase
from prime_factors import PrimeFactors


class TestPrimeFactors(TestCase):
    def test_get_prime_factors(self):
        sut = PrimeFactors()
        ret = sut.get_prime_factors(1)

        self.assertEqual(ret, [])
