import ctypes

suma = ctypes.CDLL('./testing.so')
multi = ctypes.CDLL('./testing.so')

suma.more_or_less.argtypes = (ctypes.c_int, ctypes.c_int)
suma.more_or_less.restype = (ctypes.c_int)

multi.multipl.argtypes = (ctypes.c_int, ctypes.c_int)
multi.multipl.restype = (ctypes.c_int)

result1 = suma.more_or_less(5, 7)
result2 = multi.multipl(5, 7)
print (f'5 + 7 = {result1}')
print("5 x 7 = ", result2)
