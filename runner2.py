import ctypes

lib = ctypes.CDLL("less_simple.so")

lib.square_root.restype = ctypes.c_float
lib.square_root.argtypes = [ctypes.c_float]

val = 3.0
print(f"The square root of {val} is {lib.square_root(val)}")
