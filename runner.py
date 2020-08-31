import ctypes

lib = ctypes.CDLL("simple.so")
lib.count(10)

