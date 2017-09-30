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
        #z = np.
        Z = np.identity(C.shape[0])
        L = np.zeros(C.shape[0])
        for i in range(self.n_itr):
            pass
        
if __name__ == '__main__':
    A = np.asmatrix(np.random.rand(400,300))
    C = A.T * A
    print C
    r = RIF(A);
    


            
        