import numpy as np

s = raw_input()
s = s.split(' ')
n = len(s)
A = np.array(s)

for i in range(0,n-1):
    s = raw_input()
    s = s.split(' ')
    A = np.concatenate((A, s))
A = A.reshape(n, n)
print A

# A = np.array ([[1,2, 3], [3, 4, 5],[6, 7, 8]])
# print A

def turn90left(Matrix):
    n = len(Matrix)
    B = np.zeros(shape=Matrix.shape, dtype=np.int)
    if Matrix.shape[0] != Matrix.shape[1]:
        print ('matrix is not squared')
        return
    else:
        for i in range(0, n):
            for j in range(0, n):
                B[i][j] = Matrix[j][n - i - 1]
        print B
        return B
turn90left(A)