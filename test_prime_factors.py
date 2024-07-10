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
        self.assertEqual([2, 2], self.prime_factors.of(4))

    def test_prime_factor_of_6(self):
        self.assertEqual([2, 3], self.prime_factors.of(6))

    def test_prime_factor_of_9(self):
        self.assertEqual([3, 3], self.prime_factors.of(9))

    def test_prime_factor_of_12(self):
        self.assertEqual([2, 2, 3], self.prime_factors.of(12))

    def test_prime_factor_of_1_using_recursive(self):
        self.assertEqual([], self.prime_factors.of_recursive(1))

    def test_prime_factor_of_2_using_recursive(self):
        self.assertEqual([2], self.prime_factors.of_recursive(2))

    def test_prime_factor_of_3_using_recursive(self):
        self.assertEqual([3], self.prime_factors.of_recursive(3))

    def test_prime_factor_of_4_using_recursive(self):
        self.assertEqual([2, 2], self.prime_factors.of_recursive(4))

    def test_prime_factor_of_6_using_recursive(self):
        self.assertEqual([2, 3], self.prime_factors.of_recursive(6))
