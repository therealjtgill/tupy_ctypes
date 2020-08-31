import ctypes

def callback1(n):
   for i in range(n):
      print(f"Callback1 {i}")

def callback2(n):
   for i in range(n):
      print(f"Callback2 yaaaasss {i*2}")

callback_proto = ctypes.CFUNCTYPE(None, ctypes.c_int)

callback1_c = callback_proto(callback1)
callback2_c = callback_proto(callback2)

lib = ctypes.CDLL("supermax.so")
lib.callbackExample.restype = None
lib.callbackExample.argtypes = [ctypes.c_int, callback_proto]

lib.callbackExample(10, callback1_c)
lib.callbackExample(10, callback2_c)
