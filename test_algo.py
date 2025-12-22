"""
Test suite for Python Jour 6 - Algorithmes
Unit tests for all algorithm implementations
"""

import unittest
from algo import (
    bubble_sort, quick_sort, merge_sort,
    linear_search, binary_search,
    factorial, fibonacci, is_prime,
    reverse_string, is_palindrome,
    gcd
)


class TestSortingAlgorithms(unittest.TestCase):
    """Test cases for sorting algorithms"""
    
    def setUp(self):
        """Set up test data"""
        self.unsorted = [64, 34, 25, 12, 22, 11, 90]
        self.sorted_expected = [11, 12, 22, 25, 34, 64, 90]
        self.empty = []
        self.single = [42]
        self.duplicates = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    
    def test_bubble_sort(self):
        """Test bubble sort"""
        self.assertEqual(bubble_sort(self.unsorted), self.sorted_expected)
        self.assertEqual(bubble_sort(self.empty), self.empty)
        self.assertEqual(bubble_sort(self.single), self.single)
    
    def test_quick_sort(self):
        """Test quick sort"""
        self.assertEqual(quick_sort(self.unsorted), self.sorted_expected)
        self.assertEqual(quick_sort(self.empty), self.empty)
        self.assertEqual(quick_sort(self.single), self.single)
    
    def test_merge_sort(self):
        """Test merge sort"""
        self.assertEqual(merge_sort(self.unsorted), self.sorted_expected)
        self.assertEqual(merge_sort(self.empty), self.empty)
        self.assertEqual(merge_sort(self.single), self.single)
    
    def test_duplicates(self):
        """Test sorting with duplicates"""
        expected = [1, 1, 2, 3, 4, 5, 5, 6, 9]
        self.assertEqual(bubble_sort(self.duplicates), expected)
        self.assertEqual(quick_sort(self.duplicates), expected)
        self.assertEqual(merge_sort(self.duplicates), expected)


class TestSearchAlgorithms(unittest.TestCase):
    """Test cases for search algorithms"""
    
    def setUp(self):
        """Set up test data"""
        self.array = [11, 12, 22, 25, 34, 64, 90]
        self.unsorted = [64, 34, 25, 12, 22, 11, 90]
    
    def test_linear_search_found(self):
        """Test linear search when element is found"""
        self.assertEqual(linear_search(self.array, 25), 3)
        self.assertEqual(linear_search(self.array, 11), 0)
        self.assertEqual(linear_search(self.array, 90), 6)
    
    def test_linear_search_not_found(self):
        """Test linear search when element is not found"""
        self.assertEqual(linear_search(self.array, 99), -1)
        self.assertEqual(linear_search([], 5), -1)
    
    def test_binary_search_found(self):
        """Test binary search when element is found"""
        self.assertEqual(binary_search(self.array, 25), 3)
        self.assertEqual(binary_search(self.array, 11), 0)
        self.assertEqual(binary_search(self.array, 90), 6)
    
    def test_binary_search_not_found(self):
        """Test binary search when element is not found"""
        self.assertEqual(binary_search(self.array, 99), -1)
        self.assertEqual(binary_search([], 5), -1)


class TestMathAlgorithms(unittest.TestCase):
    """Test cases for mathematical algorithms"""
    
    def test_factorial(self):
        """Test factorial calculation"""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)
    
    def test_factorial_invalid(self):
        """Test factorial with invalid input"""
        with self.assertRaises(ValueError):
            factorial(-1)
    
    def test_fibonacci(self):
        """Test Fibonacci sequence"""
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(10), 55)
    
    def test_fibonacci_invalid(self):
        """Test Fibonacci with invalid input"""
        with self.assertRaises(ValueError):
            fibonacci(-1)
    
    def test_is_prime(self):
        """Test prime number check"""
        # Prime numbers
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(97))
        
        # Non-prime numbers
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(100))
    
    def test_gcd(self):
        """Test GCD calculation"""
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(10, 5), 5)
        self.assertEqual(gcd(17, 19), 1)  # Coprime
        self.assertEqual(gcd(100, 50), 50)


class TestStringAlgorithms(unittest.TestCase):
    """Test cases for string algorithms"""
    
    def test_reverse_string(self):
        """Test string reversal"""
        self.assertEqual(reverse_string("Hello"), "olleH")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string("racecar"), "racecar")
    
    def test_is_palindrome(self):
        """Test palindrome check"""
        # Palindromes
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("Madam"))
        self.assertTrue(is_palindrome("12321"))
        
        # Non-palindromes
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("12345"))


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and special conditions"""
    
    def test_empty_arrays(self):
        """Test algorithms with empty arrays"""
        empty = []
        self.assertEqual(bubble_sort(empty), empty)
        self.assertEqual(quick_sort(empty), empty)
        self.assertEqual(merge_sort(empty), empty)
        self.assertEqual(linear_search(empty, 5), -1)
        self.assertEqual(binary_search(empty, 5), -1)
    
    def test_single_element(self):
        """Test algorithms with single element"""
        single = [42]
        self.assertEqual(bubble_sort(single), single)
        self.assertEqual(quick_sort(single), single)
        self.assertEqual(merge_sort(single), single)
        self.assertEqual(linear_search(single, 42), 0)
        self.assertEqual(binary_search(single, 42), 0)
    
    def test_negative_numbers(self):
        """Test algorithms with negative numbers"""
        negatives = [-5, 3, -1, 2, -10]
        sorted_expected = [-10, -5, -1, 2, 3]
        self.assertEqual(bubble_sort(negatives), sorted_expected)
        self.assertEqual(quick_sort(negatives), sorted_expected)
        self.assertEqual(merge_sort(negatives), sorted_expected)


def run_tests():
    """Run all tests with detailed output"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestSortingAlgorithms))
    suite.addTests(loader.loadTestsFromTestCase(TestSearchAlgorithms))
    suite.addTests(loader.loadTestsFromTestCase(TestMathAlgorithms))
    suite.addTests(loader.loadTestsFromTestCase(TestStringAlgorithms))
    suite.addTests(loader.loadTestsFromTestCase(TestEdgeCases))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.wasSuccessful():
        print("\n✅ ALL TESTS PASSED!")
    else:
        print("\n❌ SOME TESTS FAILED!")
    
    print("=" * 60)
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)
