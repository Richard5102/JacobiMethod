#!/usr/bin/env python3
import numpy as np
from numpy import linalg as la
from prettytable import PrettyTable

def Jacobi(A,b, TOL=1e-2, Nmax=50): 
  n = len(A) 
  x0 = np.zeros(n)
  x = np.zeros(n)

  names = []
  names.append('i')
  for i in range(n):
    names.append('x'+str(i + 1))
  res = PrettyTable(field_names=names)

  k = 1
  while k <= Nmax:
    for i in range(n):
      suma = 0
      for j in range(n):
        if j!=i:
          suma = suma + A[i, j]*x0[j]
        x[i] = (-suma + b[i])/A[i, i]

      res.add_row([k] + x.tolist())
    if la.norm(x - x0) < TOL:
      return print(res)

    k += 1
    x0 = np.copy(x)
    
  print("El método no converge")
  return print(res)
