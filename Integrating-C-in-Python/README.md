## English 🇬🇧

# Integrating-C-in-Python
"Step-by-step tutorial on how to integrate C code into Python to improve application performance and take advantage of low-level libraries. Includes practical examples with ctypes."

# Integrating C in Python: A Step-by-Step Guide

This repository provides a simple tutorial on how to integrate C code into Python using `ctypes`. You'll learn how to call C functions from Python to improve performance or access lower-level operations, making your Python code faster and more powerful.

## Why Integrate C with Python?

Combining C with Python allows you to:
- **Boost Performance**: Execute critical functions faster with C while maintaining the simplicity of Python.
- **Reuse Existing C Libraries**: Access a wide range of powerful libraries written in C.
- **Handle Low-Level Operations**: Interact directly with hardware or optimize memory usage in Python projects.

## What's in this Tutorial?

1. **Basic C Function Example**: 
   Learn how to create a simple C function that can be called from Python using `ctypes`.
   
2. **Compiling C Code**: 
   Instructions for compiling the C code into a shared library on Linux, macOS, and Windows.

3. **Calling C Functions in Python**: 
   Write Python code that loads and executes the C function, passing arguments and receiving return values.

## Getting Started

### Prerequisites

- Basic knowledge of Python and C.
- GCC or a similar C compiler (for compiling C code).
- Python installed on your system.

### Example Code

#### Step 1: Writing the C Code

Create a file called `mylib.c` with the following content:

```c
#include <stdio.h>

int add_numbers(int a, int b) {
    return a + b;
}
```

#### Step 2: Compiling the C Code

Compile the C code into a shared library. On Linux or macOS, run:
```
gcc -shared -o mylib.so -fPIC mylib.c
```
For Windows, you may need to adjust the command to:

```
gcc -shared -o mylib.dll -fPIC mylib.c

```
#### Step 3: Writing the Python Code

Create a Python script `main.py`:
```py
import ctypes

# Load the shared library
mylib = ctypes.CDLL('./mylib.so')

# Define argument and return types for the C function
mylib.add_numbers.argtypes = (ctypes.c_int, ctypes.c_int)
mylib.add_numbers.restype = ctypes.c_int

# Call the C function from Python
result = mylib.add_numbers(5, 7)
print(f"Result of adding 5 and 7 in C: {result}")
```

#### Running the Example

- Compile the C code.
- Run the Python script:
```
python3 main.py
```
#### Expected Output
```
Result of adding 5 and 7 in C: 12
```
#### License
This tutorial is open-source and available under the MIT License.
