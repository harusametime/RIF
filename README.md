# Robust Incomplete Factorization

Robust Incomplete Factorization (RIF) is known as a method for generating a preconditioner for a linear system *Ax = b*. RIF outputs matrices *L* and *Z* that hold:

<p align="center"><img src="https://latex.codecogs.com/gif.latex?Z^T&space;C&space;Z&space;\approx&space;I,&space;I&space;\approx&space;L^T&space;Z,&space;C&space;=&space;A^T&space;A" title="Z^T C Z \approx I, I \approx L^T Z, C = A^T A" />
</p>

*L^T* is the transposed Cholesky factor of *C* and *Z* is the inverse matrix. 
