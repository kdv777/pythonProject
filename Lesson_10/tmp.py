import numpy

matrix_data1 = [[31, 32], [37, 43], [51, 86]]
matrix_data2 = [[17, 15], [21, 32], [11, 23]]

a = numpy.array(matrix_data1)
b = numpy.array(matrix_data2)
# a= cycle(matrix_data1)
# print(a)
# print(next(a))
print(a)
print(b)
c = a + b
print(c)