import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity

def proximity(A):
    
    print('A:')
    print(A)
    print()
    
    B=A.T
    print('Transpose of A:')
    print(B)
    print()

    Q=A@B
    print('One-mode projection:')
    print(Q)
    print()
    
    investingproximity = Q * 0.1
    print('Normalized One-mode projection:')
    print(investingproximity)
    
    np.savetxt('investmentproximity.txt', investingproximity)
    
#investingproximity
#proximity(np.array([[0,0,0,1,0,0,0,0,0,0],[0,0,1,0,1,0,0,0,1,0],[0,0,1,0,0,0,0,0,0,0],[0,1,0,1,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,0,1,0,1,0,0,1],[0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,1,0],[1,1,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,1],[0,0,1,0,0,0,0,0,0,0],[0,0,0,1,1,0,1,1,1,1],[0,0,0,0,1,0,0,0,0,0],[0,1,1,0,1,0,0,0,1,0],[1,1,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,1],[0,0,1,0,0,0,0,0,0,1],[1,0,0,1,1,0,1,0,0,0],[0,0,0,0,0,0,0,1,0,0],[1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,1,0,1,0],[1,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,0,1,0,0],[0,0,1,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1,0,0],[1,1,1,0,0,0,0,1,0,0],[0,1,0,1,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,0,0]]))