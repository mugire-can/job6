"""
Python Jour 6 - Algorithmes
Main algorithm implementations for Day 6 programming exercises.

This module contains solutions for algorithmic problems including:
- Sorting algorithms
- Searching algorithms
- Data structure operations
- Problem-solving approaches
"""


def bubble_sort(arr):
    """
    Bubble Sort Algorithm
    
    Time Complexity: O(n²)
    Space Complexity: O(1)
    
    Args:
        arr: List of comparable elements
        
    Returns:
        Sorted list
        
    Example:
        >>> bubble_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    n = len(arr)
    arr = arr.copy()
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    
    return arr


def quick_sort(arr):
    """
    Quick Sort Algorithm
    
    Time Complexity: O(n log n) average, O(n²) worst
    Space Complexity: O(log n)
    
    Args:
        arr: List of comparable elements
        
    Returns:
        Sorted list
        
    Example:
        >>> quick_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr):
    """
    Merge Sort Algorithm
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Args:
        arr: List of comparable elements
        
    Returns:
        Sorted list
        
    Example:
        >>> merge_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return _merge(left, right)


def _merge(left, right):
    """Helper function for merge sort"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def linear_search(arr, target):
    """
    Linear Search Algorithm
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        arr: List to search
        target: Element to find
        
    Returns:
        Index of element if found, -1 otherwise
        
    Example:
        >>> linear_search([10, 20, 30, 40, 50], 30)
        2
    """
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1


def binary_search(arr, target):
    """
    Binary Search Algorithm (requires sorted array)
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    Args:
        arr: Sorted list to search
        target: Element to find
        
    Returns:
        Index of element if found, -1 otherwise
        
    Example:
        >>> binary_search([10, 20, 30, 40, 50], 30)
        2
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def factorial(n):
    """
    Calculate factorial of n
    
    Time Complexity: O(n)
    Space Complexity: O(n) due to recursion
    
    Args:
        n: Non-negative integer
        
    Returns:
        Factorial of n
        
    Example:
        >>> factorial(5)
        120
    """
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """
    Calculate nth Fibonacci number (optimized)
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        n: Position in Fibonacci sequence
        
    Returns:
        nth Fibonacci number
        
    Example:
        >>> fibonacci(6)
        8
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def is_prime(n):
    """
    Check if number is prime
    
    Time Complexity: O(√n)
    Space Complexity: O(1)
    
    Args:
        n: Integer to check
        
    Returns:
        True if prime, False otherwise
        
    Example:
        >>> is_prime(17)
        True
        >>> is_prime(10)
        False
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def reverse_string(s):
    """
    Reverse a string
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        s: String to reverse
        
    Returns:
        Reversed string
        
    Example:
        >>> reverse_string("Hello")
        'olleH'
    """
    return s[::-1]


def is_palindrome(s):
    """
    Check if string is palindrome (ignoring spaces and case)
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        s: String to check
        
    Returns:
        True if palindrome, False otherwise
        
    Example:
        >>> is_palindrome("A man a plan a canal Panama")
        True
    """
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


def gcd(a, b):
    """
    Calculate Greatest Common Divisor using Euclidean algorithm
    
    Time Complexity: O(log(min(a, b)))
    Space Complexity: O(1)
    
    Args:
        a, b: Integers
        
    Returns:
        GCD of a and b
        
    Example:
        >>> gcd(48, 18)
        6
    """
    while b:
        a, b = b, a % b
    return abs(a)


# Main execution
if __name__ == "__main__":
    print("=" * 60)
    print("Python Jour 6 - Algorithmes")
    print("=" * 60)
    
    # Example usage
    test_array = [64, 34, 25, 12, 22, 11, 90]
    
    print("\nOriginal array:", test_array)
    print("Bubble Sort:", bubble_sort(test_array))
    print("Quick Sort:", quick_sort(test_array))
    print("Merge Sort:", merge_sort(test_array))
    
    # Search examples
    sorted_array = [11, 12, 22, 25, 34, 64, 90]
    target = 25
    print(f"\nLinear Search for {target}:", linear_search(test_array, target))
    print(f"Binary Search for {target}:", binary_search(sorted_array, target))
    
    # Number algorithms
    print("\nNumber Algorithms:")
    print("Factorial(5):", factorial(5))
    print("Fibonacci(6):", fibonacci(6))
    print("Is 17 prime?:", is_prime(17))
    print("GCD(48, 18):", gcd(48, 18))
    
    # String algorithms
    print("\nString Algorithms:")
    print("Reverse 'Hello':", reverse_string("Hello"))
    print("Is 'A man a plan a canal Panama' palindrome?:", 
          is_palindrome("A man a plan a canal Panama"))
    
    print("\n" + "=" * 60)
    print("✅ All algorithms executed successfully!")
    print("=" * 60)
