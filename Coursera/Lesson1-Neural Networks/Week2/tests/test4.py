import numpy as np

a = np.ones((3,4))
b = np.ones((4,1))
# a.shape = (3,4)
# b.shape = (4,1)

c = np.zeros_like(a)

for i in range(3):
  for j in range(4):
    c[i][j] = a[i][j] + b[j]

print(c)

d = a+b.T
print(d)
