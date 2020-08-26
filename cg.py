# Libraries
from mpi4py import MPI
from scipy.sparse import rand
import numpy
from sys import argv
import dotProduct as dp

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


# Input Parameters
dimension = int(argv[1])
sparsity = float(argv[2])

# Initial Matrix and Vectors

A = rand(dimension, dimension, density=sparsity, format="csr")
A = A + A.T
x = numpy.zeros(dimension)
x[0] = 1
b = numpy.random.rand(dimension)


# Iterate
r = b - A.dot(x)
print(r)
p = r.copy()

for i in range(0,10):
    Ap = A.dot(p)
    #Ap = dp.matrixproduct(A,p)
    top = numpy.dot(r.T, r)
    bottom = numpy.dot(p.T, Ap)
    alpha = top / bottom

    x = x + alpha * p
    r = r - alpha * Ap

    norm_value = numpy.linalg.norm(r)
    if norm_value < 1e-8:
        print("x =", x)
        break
    new_top = numpy.dot(r.T, r)
    beta = new_top/top
    p = r + beta * p

print("Done in :", i, "iterations. Norm value: ", norm_value)