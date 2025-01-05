# Databricks (🐍 Pythonic Data Structures)

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/-Pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)

This library is a collection of data structures that are not included in the Python standard library. The goal is to provide a Pythonic interface to these data structures, making them easier to use and more intuitive.

## Why did I create this library?

I created this library because I wanted to learn more about data structures and algorithms. I also wanted to create a library that would be useful to other Python developers. I hope that this library will help you learn more about data structures and algorithms, and that it will be useful in your own projects.

## Features

-  **Custom Data Structures**: Implementations of data structures like heaps, tries, and graphs that are not part of the standard library.
-  **Pythonic Interfaces**: Designed with a focus on usability and readability, following Python's idiomatic conventions.
-  **Efficiency**: Optimized for performance with a focus on minimizing time and space complexity.
-  **Extensibility**: Easily extendable to include new data structures or modify existing ones.

## Installation

You can clone the repository and install it manually:

```bash
git clone https://github.com/nicholasadamou/databricks.git
cd databricks
python setup.py install
```

This library is not part of [PyPI](https://pypi.org/) because the name `databricks` has already been used, so you will need to install it manually.

## Usage

Here's a quick example of how to use one of the data structures in this library:

```python
from databricks import Heap

heap = Heap()
heap.insert(10)
heap.insert(5)
heap.insert(20)

print(heap.extract_min())  # Outputs: 5
```

## Testing

To ensure the reliability and correctness of the library, a comprehensive suite of tests is included. You can run the tests using `pytest`:

1. Install `pytest` if you haven't already:

    ```bash
    pip install pytest
    ```

2. Run the tests:

    ```bash
    pytest
    ```

This will find and execute all the test cases and provide a summary of the results.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
