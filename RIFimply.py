'''
Created on 2017/09/30
@author: Masaki Samejima
'''

import numpy as np
import scipy.sparse.linalg
from scipy.sparse import lil_matrix, coo_matrix, csc_matrix, identity
import time

'''
Left-looking Gram-Schmidt process for robust incomplete factorization

Reference:
    Algorithm 5 in 
    Jennifer Scott and Miroslav Tuma:
    Preconditioning of Linear Least Squares by Robust Incomplete Factorization for Implicitly Held Normal Equations
    SIAM J. Sci. Comput., 38(6), C603-C623 (2016)
    Read More: http://epubs.siam.org/doi/abs/10.1137/16M105890X?journalCode=sjoce3
'''
class RIFimply(object):
    
    def __init__(self, A, tol = 0.1):
        '''
        Constructor
        '''
        self.A = A
        self.tol = tol
        self.shift = 0.1
        
    def factorize(self):
        
        size = self.A.shape[1]
         
        # Lower triangle matrix L
        L = lil_matrix((size,size))
        _Z = lil_matrix((size,size))
         
        #Compute a column scaling S
        s_diag = scipy.sparse.linalg.norm(self.A, axis = 0)
        s_diag = np.power(s_diag,-1)
        S = scipy.sparse.diags(s_diag)
        
        # Scaling A
        self.A = self.A * S
        
        # Initialize L & Z
        #L[0,:] =  (1+self.shift)* scipy.sparse.linalg.norm(self.A[0,:]) # looks strange for lower triangle. L[0,0]?
        L[0,0] =  (1+self.shift)* scipy.sparse.linalg.norm(self.A[0,:]) 
        Z = identity(size, format = "csc")
       
        
        print(size)
        for k in range(size-1):
            ck = self.A[:,:k+1].T.dot(self.A[:, k+1])
            
            # J is a set of all candidate vertices that are reachable c_k
            J = (L[:k+1, :k+1]*ck).nonzero()[0]
            
            #Then vertices in J are pruned (currently skipped)
            
            for j in J:
                print(j)
                
                #MGS case
                v = Z[:,j]
                u = _Z[:k]
            
            
        
if __name__ == '__main__':
    
    
    matrix_size = np.array([5,4])
    matrix_density = 1
    
    A = scipy.sparse.rand(matrix_size[0],matrix_size[1], density = matrix_density, format = 'csr') 
    r = RIFimply(A);
    Z, L = r.factorize()
    print(time.process_time())