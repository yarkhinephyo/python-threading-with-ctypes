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
python test_prime_python.py

# Python function with threading module
python test_prime_python_threading.py

# C function through ctypes
python test_prime_ctypes.py

# C function with pthreads through ctypes
python test_prime_ctypes_pthread.py

# C function with Python threading module
python test_prime_ctypes_threading.py
```