'''
Created on 2017/09/30
@author: Masaki Samejima
'''

import numpy as np
import scipy.sparse.linalg
from scipy.sparse import lil_matrix

'''
Left-looking Gram-Schmidt process for robust incomplete factorization

Reference:
    Jennifer Scott and Miroslav Tuma:
    Preconditioning of Linear Least Squares by Robust Incomplete Factorization for Implicitly Held Normal Equations
    SIAM J. Sci. Comput., 38(6), C603-C623 (2016)
    Read More: http://epubs.siam.org/doi/abs/10.1137/16M105890X?journalCode=sjoce3
'''
class RIF(object):

    def __init__(self, C, tol = 0.1):
        '''
        Constructor
        '''
        self.C = C
        self.tol = tol
        
    def factorize(self):
        size = C.shape[0]
        print("a")
        Z = lil_matrix((size,size))
        print("b")
        L = lil_matrix((size,size))
        
        print("c")
        _Z =[lil_matrix((size,size)) for i in range(size)]
        _Z[0][:,:] = np.identity(size)
        
        
        print("d")
        
        for k in range(size):             
            if k > 0:
                for j in range(k):
                    L[j,k] = self.Cinner(_Z[j,:,k],Z[:,j])
                    _Z[j+1,:,k] = _Z[j,:,k] - L[j,k]*Z[:,j]
            
            L[k,k] = self.Cnorm(_Z[k,:,k])
            Z[:,k]= _Z[k,:,k] / L[k,k]
       
        return Z, L
    
    def Cinner(self, x, y):
        #return np.matmul(np.matmul(x.T, self.C), y)
        return x.T *self.C *y
        
    def Cnorm(self, x):
        return np.sqrt(self.Cinner(x,x))
        
if __name__ == '__main__':
    #A = np.asmatrix(np.random.rand(5,4))
    matrix_size = np.array([20000,10000])
    matrix_density = 0.01
    A = scipy.sparse.rand(matrix_size[0],matrix_size[1], density = matrix_density ) 
    C = A.T * A

    r = RIF(C);
    Z, L = r.factorize()
    
    '''
    Testing result
    - L^T is the Cholesky factor of C
    - L^T Z = I
    - Z^T C Z = I
    '''
    print("L^T")
    print(L.T)
    print("Cholesky factor")
    print(np.linalg.cholesky(C))
    print("-----------------------------------------------")
    print("L^T *Z")
    print(L.T * Z)
    print("-----------------------------------------------")
    print("Z^T*C*Z")
    print(Z.T*C*Z)

    