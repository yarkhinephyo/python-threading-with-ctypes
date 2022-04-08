## CTypes Demo

Code for demonstrating the usage of `ctypes` to speed up Python code. Blog post [here](https://yarkhinephyo.github.io/blog/notes/2022/04/05/speed-up-python-with-ctypes.html).

## Usage

Install GNU Make.

```
make compile
```

Test the timings with Python (3.8 used).

```bash
# Python function only
python -m timeit -n 5 -s 'import test_python as t' 't.timeit_function()'

# Python function with threading module
python -m timeit -n 5 -s 'import test_python_threading as t' 't.timeit_function()'

# C function through ctypes
python -m timeit -n 5 -s 'import test_ctypes as t' 't.timeit_function()'

# C function with pthreads through ctypes
python -m timeit -n 5 -s 'import test_ctypes_pthread as t' 't.timeit_function()'

# C function with Python threading module
python -m timeit -n 5 -s 'import test_ctypes_threading as t' 't.timeit_function()'
```