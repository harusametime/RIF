'''
Created on 2017/09/30

@author: Masaki Samejima
'''

import numpy as np


class RIF(object):
    '''
    classdocs
    '''

    def __init__(self, C, maxitr = 1000):
        '''
        Constructor
        '''
        self.C = C
        self.n_itr = maxitr
        
    def factorize(self):
        size = C.shape[0]
        Z = np.zeros((size,)*2)
        L = np.zeros((size,)*2)
        _Z = np.zeros((size,)*3)
        
        for k in range(size):
            _Z[0,:,:] = np.identity(size)            
            if k > 0:
                for j in range(k-1):
                    L[k,j] = self.Cinner(_Z[j,k,:],Z[j,:])
                    _Z[j+1,k,:] = _Z[j,k,:] - L[k,j]*Z[j,:]
            
            L[k,k] = self.Cnorm(_Z[0,k,:])
            Z[k,:]= _Z[k,k,:] / L[k,k]
            
        return Z
    
    def Cinner(self, x, y):
        return np.matmul(np.matmul(x.T, self.C), y)
        
    def Cnorm(self, x):
        return np.sqrt(self.Cinner(x,x))
        
if __name__ == '__main__':
    A = np.asmatrix(np.random.rand(400,300))
    C = A.T * A
    r = RIF(C);
    Z = r.factorize()
    