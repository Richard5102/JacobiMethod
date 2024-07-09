#!/usr/bin/env python3
import numpy as np
import moduleEjemplo

A = np.array([[3,-1,1],[3,6,2],[3,3,7]])
B = np.array([1,0,4])
moduleEjemplo.Jacobi(A,B)
