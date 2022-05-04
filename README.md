# bst

![CI](https://github.com/wpwilkes/bsa/actions/workflows/python-package.yml/badge.svg?branch=develop)

Basic Sorting Algorithms

## Installation

Clone the repository using https://github.com/wpwilkes/bsa.git.
Use `pip` to run the installation process.

```bash
pip install path/to/bsa/
```

## Test

After installing the package, be sure to run the tests to ensure the
software works as intended.

```bash
pytest path/to/tests/
```

## Usage

```python
import bsa

list_to_sort = [3, 1, 2]
bsa.bubble_sort(list_to_sort)
list_to_sort
# [1, 2, 3]
```
