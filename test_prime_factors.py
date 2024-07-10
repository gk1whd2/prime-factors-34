from unittest import TestCase
from prime_factors import PrimeFactors


class TestPrimeFactors(TestCase):
    def setUp(self):
        super().setUp()
        self.prime_factors = PrimeFactors()

    def test_get_prime_factors(self):
        ret = self.prime_factors.of(1)

        self.assertEqual(ret, [])


    def test_prime_factor_of_2(self):
        self.assertEqual([2], self.prime_factors.of(2))

    def test_prime_factor_of_3(self):
        self.assertEqual([3], self.prime_factors.of(3))

    def test_prime_factor_of_4(self):
        self.assertEqual([2,2], self.prime_factors.of(4))

