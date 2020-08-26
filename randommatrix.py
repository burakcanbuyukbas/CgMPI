import random
import sys
from scipy.sparse import rand
import numpy
from sys import argv

# Input Parameters
dimension = int(argv[1])
sparsity = float(argv[2])
x0 = []
# Initial Matrix and Vectors
A = rand(dimension, dimension, density=sparsity, format="csr")
A = A + A.T
x = numpy.zeros(dimension)
x[0] = 1
b = numpy.random.rand(dimension)

# Iterate
r = b - A.dot(x)
p = r.copy()
for i in range(0, 100):
    Ap = A.dot(p)
    top = numpy.dot(r.T, r)
    bottom = numpy.dot(p.T, Ap)
    alpha = top / bottom

    x = x + alpha * p
    r = r - alpha * Ap

    norm_value = numpy.linalg.norm(r)
    if norm_value < 1e-8:
        x0.append(x)
        break
    new_top = numpy.dot(r.T, r)
    beta = new_top / top
    p = r + beta * p

if (len(sys.argv) > 1):

    M = int(sys.argv[1])
    N = M

    ans = [0 for i in range(M)]
    b = [0 for i in range(M)]
    table2 = [[0 for i in range(N)] for j in range(M)]

    for i in range(M):
        ans[i] = random.random()
        b[i] = 0

    for i in range(M):
        for j in range(N):
            if i <= j:
                table2[i][j] = random.random()
                if i < j:
                    if random.random() < 0.95:
                        table2[i][j] = 0
                table2[j][i] = table2[i][j]

    f = open('matrix', 'w');
    for i in range(M):
        for j in range(N):
            ##table2[i][j] = random.random()
            f.write(str(table2[i][j]))
            f.write('\t')
            b[i] += table2[i][j] * ans[j]
        f.write('\n')
    f.close()

    f = open('ans', 'w')
    f.write("Done in: " + str(i) + " iteration. Norm Value: " + str(norm_value))
    f.write('\n')
    out = x0[-1]
    f.write(str(out))
    f.write('\n')
    f.close()




else:

    print("please input a number")