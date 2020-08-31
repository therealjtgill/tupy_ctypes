import ctypes

lib = ctypes.CDLL("maximum.so")

class InputType(ctypes.Structure):
   _fields_ = [
      ("a", ctypes.c_float*3),
      ("b", ctypes.c_int)
   ]

class OutputType(ctypes.Structure):
   _fields_ = [
      ("u", ctypes.c_float*3),
      ("v", ctypes.c_uint8),
      ("w", ctypes.c_float)
   ]

lib.returnSillyThings.restype = OutputType
lib.returnSillyThings.argtypes = [ctypes.POINTER(InputType)]

lib.outArgsSillyThings.restype = None
lib.outArgsSillyThings.argtypes = [
   ctypes.POINTER(InputType),
   ctypes.POINTER(OutputType)
]

in1 = InputType()
in1.a[0] = 1.0
in1.a[1] = 2.0
in1.a[2] = 3.0
in1.b = 567

out_thing1 = lib.returnSillyThings(ctypes.byref(in1))
print(out_thing1.u[0], out_thing1.u[1], out_thing1.u[2])
print(out_thing1.v)
print(out_thing1.w)

out_thing2 = OutputType()
lib.outArgsSillyThings(ctypes.byref(in1), ctypes.byref(out_thing2))

print(out_thing2.u[0], out_thing2.u[1], out_thing2.u[2])
print(out_thing2.v)
print(out_thing2.w)
