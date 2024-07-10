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
    def test_prime_factor_of_5_using_recursive(self):
        self.assertEqual([5], self.prime_factors.of_recursive(5))

    def test_prime_factor_of_recursive_with_prime_numbers(self):
        self.assertEqual([2], self.prime_factors.of_recursive(2))
        self.assertEqual([3], self.prime_factors.of_recursive(3))
        self.assertEqual([5], self.prime_factors.of_recursive(5))
        self.assertEqual([7], self.prime_factors.of_recursive(7))
        self.assertEqual([11], self.prime_factors.of_recursive(11))
        self.assertEqual([13], self.prime_factors.of_recursive(13))
        self.assertEqual([17], self.prime_factors.of_recursive(17))
        self.assertEqual([19], self.prime_factors.of_recursive(19))
        self.assertEqual([23], self.prime_factors.of_recursive(23))
        self.assertEqual([29], self.prime_factors.of_recursive(29))


    def test_prime_factor_of_recursive_with_none_prime_numbers(self):
        self.assertEqual([2,2], self.prime_factors.of_recursive(4))
        self.assertEqual([2,3], self.prime_factors.of_recursive(6))
        self.assertEqual([2,2,2], self.prime_factors.of_recursive(8))
        self.assertEqual([3,3], self.prime_factors.of_recursive(9))
        self.assertEqual([2,2,3], self.prime_factors.of_recursive(12))
        self.assertEqual([2,7], self.prime_factors.of_recursive(14))
        self.assertEqual([3,5], self.prime_factors.of_recursive(15))
        self.assertEqual([3,7], self.prime_factors.of_recursive(21))
        self.assertEqual([5,5], self.prime_factors.of_recursive(25))
        self.assertEqual([2,2,7], self.prime_factors.of_recursive(28))
        self.assertEqual([2,2,2,2,2], self.prime_factors.of_recursive(32))
        self.assertEqual([3,11], self.prime_factors.of_recursive(33))
        self.assertEqual([3,13], self.prime_factors.of_recursive(39))
        self.assertEqual([2,3,7], self.prime_factors.of_recursive(42))
        self.assertEqual([3,17], self.prime_factors.of_recursive(51))

