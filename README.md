## CTypes Demo

Install GNU Make to compile the shared libary files.

```
make compile
```

Test the timings with Python.

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