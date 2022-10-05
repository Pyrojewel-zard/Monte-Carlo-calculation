from ctypes import *
great_module = cdll.LoadLibrary('./libpycallcpp.dll')

great_module.trapezoid.restype = c_double
great_module.simpson.restype = c_double
great_module.gauss.restype = c_double
great_module.gauss2.restype = c_double

print(great_module.trapezoid(c_double(0),c_double(1),c_int(100)))
print(great_module.simpson(c_double(0),c_double(1),c_int(100)))
print(great_module.gauss(c_double(0),c_double(1),c_int(5)))
print(great_module.gauss2(c_double(0),c_double(1),c_int(5)))