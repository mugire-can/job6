# Python Jour 6 - Algorithmes 🐍

Complete Python algorithm implementations for Day 6 programming exercises.

[![Python 3.7+](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Complete](https://img.shields.io/badge/Status-Complete-green.svg)](#status)

---

## 📚 Overview

This project implements **11 core algorithms** with **19 comprehensive unit tests**. All code is well-documented, follows PEP 8 standards, and includes examples for each algorithm.

**Perfect for learning Python algorithms, Git workflows, and testing best practices.**

---

## ✨ Features

- ✅ **11 Algorithms** - Sorting, Searching, Math, String operations
- ✅ **19 Unit Tests** - 100% pass rate with edge case coverage
- ✅ **Complete Documentation** - Docstrings and usage examples
- ✅ **Professional Code** - PEP 8 compliant, clean structure
- ✅ **Git Workflow** - Complete Git instructions (16 jobs)
- ✅ **Learning Path** - Step-by-step tutorial files

---

## 🎯 Project Goals

- Implement efficient algorithms with clear logic
- Write clean, well-documented Python code
- Master Git version control workflow
- Understand testing and code quality
- Learn algorithmic thinking

---

## 📁 Project Structure

```
job6/
├── README.md                  # This file
├── .gitignore                # Git configuration
├── algo.py                   # 11 Algorithm implementations
├── test_algo.py              # 19 Unit tests
├── COMMANDS_REFERENCE.txt    # Complete commands guide
├── JOB1.txt - JOB16.txt     # Step-by-step tutorial
└── Python Jour 6- Algo.pdf  # Original specification
```

---

## 🚀 Quick Start

### Clone Repository

```bash
# Clone development branch (recommended)
git clone -b development https://github.com/mugire-can/job6.git
cd job6

# Or clone all branches
git clone https://github.com/mugire-can/job6.git
cd job6
git checkout development
```

### Run Algorithms

```bash
# Execute all algorithms with examples
python algo.py

# Expected: All 11 algorithms run successfully
```

### Run Tests

```bash
# Run complete test suite (19 tests)
python test_algo.py

# Expected: 19/19 tests pass ✅
```

---

## 📋 Algorithms Implemented

### Sorting Algorithms (3)

| Algorithm | Time Complexity | Space | Use Case |
|-----------|-----------------|-------|----------|
| **Bubble Sort** | O(n²) | O(1) | Learning/small arrays |
| **Quick Sort** | O(n log n) avg | O(log n) | General purpose |
| **Merge Sort** | O(n log n) | O(n) | Stable sort needed |

### Searching Algorithms (2)

| Algorithm | Time Complexity | Space | Requirement |
|-----------|-----------------|-------|-------------|
| **Linear Search** | O(n) | O(1) | Any array |
| **Binary Search** | O(log n) | O(1) | Sorted array |

### Math Algorithms (4)

| Algorithm | Time Complexity | Space | Purpose |
|-----------|-----------------|-------|---------|
| **Factorial** | O(n) | O(n) | Combinatorics |
| **Fibonacci** | O(n) | O(1) | Sequence generation |
| **Prime Check** | O(√n) | O(1) | Number validation |
| **GCD** | O(log n) | O(1) | Number theory |

### String Algorithms (2)

| Algorithm | Time Complexity | Space | Use Case |
|-----------|-----------------|-------|----------|
| **String Reverse** | O(n) | O(n) | String manipulation |
| **Palindrome Check** | O(n) | O(1) | Text validation |

---

## 🧪 Testing

### Run All Tests

```bash
python test_algo.py
```

**Expected Output:**
```
Ran 19 tests in 0.030s
OK
✅ ALL TESTS PASSED!
```

### Test Coverage

- **Sorting Tests (4)** - Normal cases, duplicates
- **Searching Tests (4)** - Found/not found cases
- **Math Tests (6)** - Valid/invalid inputs
- **String Tests (2)** - Various strings
- **Edge Cases (3)** - Empty, single, negative

### Run Specific Tests

```bash
# Run sorting tests only
python -m unittest test_algo.TestSortingAlgorithms -v

# Run specific test
python -m unittest test_algo.TestMathAlgorithms.test_fibonacci -v
```

---

## 📖 How to Use Algorithms

### Import All

```python
from algo import (
    bubble_sort, quick_sort, merge_sort,
    linear_search, binary_search,
    factorial, fibonacci, is_prime, gcd,
    reverse_string, is_palindrome
)
```

### Example: Sorting

```python
array = [64, 34, 25, 12, 22, 11, 90]
result = merge_sort(array)
print(result)  # [11, 12, 22, 25, 34, 64, 90]
```

### Example: Searching

```python
sorted_array = [11, 12, 22, 25, 34, 64, 90]
index = binary_search(sorted_array, 25)
print(index)  # 3 (position of element)
```

### Example: Math

```python
print(factorial(5))           # 120
print(fibonacci(10))          # 55
print(is_prime(17))           # True
print(gcd(48, 18))            # 6
```

### Example: String

```python
print(reverse_string("Hello"))  # olleH
print(is_palindrome("racecar")) # True
```

---

## 📚 Complete Tutorial

This repository includes **16 individual job files** for learning:

| Job | Topic | Time |
|-----|-------|------|
| JOB1-5 | Git Basics | 5 min |
| JOB6-10 | Git Advanced | 10 min |
| JOB11-15 | Python Algorithms | 10 min |
| JOB16 | Project Overview | 2 min |

**Start with JOB1.txt and follow in order!**

---

## 💻 Requirements

- **Python 3.7+**
- **No external dependencies** - Uses only Python stdlib
- **Git** (for version control)

---

## 📝 Code Style

All code follows these standards:

- ✅ **PEP 8** - Python style guidelines
- ✅ **Docstrings** - All functions documented
- ✅ **Type hints** - Where applicable
- ✅ **Comments** - Complex logic explained
- ✅ **Examples** - Usage in docstrings

---

## 📊 Repository Statistics

| Metric | Value |
|--------|-------|
| **Algorithms** | 11 |
| **Tests** | 19 |
| **Test Pass Rate** | 100% |
| **Code Lines** | ~359 |
| **Test Lines** | ~227 |
| **Documentation Files** | 20+ |
| **Git Commits** | 10+ |
| **Branches** | 3 |

---

## 🤝 Contributing

### Add New Algorithm

1. Add function to `algo.py`:
   ```python
   def new_algorithm(data):
       """Description and usage example."""
       # Implementation
       return result
   ```

2. Add tests to `test_algo.py`:
   ```python
   def test_new_algorithm(self):
       # Test cases
       self.assertEqual(result, expected)
   ```

3. Run tests: `python test_algo.py`

4. Commit and push:
   ```bash
   git add algo.py test_algo.py
   git commit -m "feat: Add new algorithm"
   git push origin development
   ```

### Workflow

```bash
# Create feature branch
git checkout -b feature/algorithm-name

# Make changes
# Test: python test_algo.py

# Commit
git add .
git commit -m "feat: Add algorithm"

# Push
git push origin feature/algorithm-name

# Create pull request on GitHub
```

---

## 🐛 Troubleshooting

### Tests Fail

```bash
# Make sure you're in the correct directory
cd job6

# Check Python version
python --version  # Should be 3.7+

# Run tests with verbose output
python -m unittest test_algo -v
```

### Import Errors

```bash
# Ensure algo.py is in the same directory
ls algo.py

# Try explicit import
python -c "from algo import bubble_sort; print(bubble_sort([3,1,2]))"
```

### Git Issues

```bash
# Check branch
git branch

# Check status
git status

# View remote
git remote -v
```

---

## 📖 Documentation Files

| File | Purpose |
|------|---------|
| **README.md** | This guide (overview, quick start) |
| **algo.py** | Algorithm implementations with docstrings |
| **test_algo.py** | Test suite with examples |
| **COMMANDS_REFERENCE.txt** | Complete Git & Python commands (62 jobs) |
| **JOB1.txt - JOB16.txt** | Step-by-step tutorial files |
| **.gitignore** | Git ignore rules |

---

## 🔗 Links

- **GitHub Repository**: https://github.com/mugire-can/job6
- **Development Branch**: https://github.com/mugire-can/job6/tree/development
- **Python Docs**: https://docs.python.org/3/
- **Git Tutorial**: https://git-scm.com/book/en/v2

---

## 📄 License

This project is released under the **MIT License**.

---

## ✅ Status

| Component | Status | Date |
|-----------|--------|------|
| **Algorithms** | ✅ Complete | 2025-12-23 |
| **Tests** | ✅ Complete (19/19) | 2025-12-23 |
| **Documentation** | ✅ Complete | 2025-12-23 |
| **Git Setup** | ✅ Complete | 2025-12-23 |
| **Jobs Tutorial** | ✅ Complete (16) | 2025-12-23 |
| **GitHub** | ✅ Released | 2025-12-23 |

---

## 👤 Author

Created as a learning exercise for Python Jour 6 - Algorithmes.

**Repository**: https://github.com/mugire-can/job6  
**Branch**: development  
**Last Updated**: 2025-12-23

---

## 🎯 Next Steps

1. **Learn**: Read JOB1.txt through JOB16.txt
2. **Explore**: Study `algo.py` implementations
3. **Test**: Run `python test_algo.py`
4. **Experiment**: Modify and add algorithms
5. **Share**: Push your changes to GitHub

---

**Happy Learning! 🚀**
