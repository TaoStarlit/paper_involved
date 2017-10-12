'''
low dimensional representation shared across a set of multiple related tasks

Study the paper:
que? what is the loss function and "正则项来控制模型复杂度"(from Weijie) exactlly?

ans: loss function is empirical error: ax <--> y;  


Problem formulation: 
1\ funtions f_t are related so that they all share a small set of features.
    [index:   i: 1-->d the original high dimension;   t: a small set of features]
    f_t(x) = sigma_i=1->d (a_it h_i(x)), t belongs to IN_T
        h_i: IR'd --> IR are features and a_it belong to IR are regression parameters.
        Our main assumption is that all the features but a few have zero coefficients across all the tasks.
    --  For simplicity, we only focus on linear features, that is h_i(x)=<u_i,x>, where u_i belong to IR'd.
    (--  Extensions to nonlinear,  for example, by using kernels along the lines[8][15])
        In addition, we assume that the vector u_i are orthonormal.
        what is orthonormal vectors?{
        }
        U denotes the dxd matrix with columns the vectors u_i, then U belong to O'd.
        The function are linear as well, that is f_t(x)=<w_t,x>, where w_t=sigma_i (a_it u_i)

        W (dxT matrix) whose columns are the vectors w_t and by A the dxT matrix with entries a_it
        We then have W_dT = U_dd A_dT   ----- W_dT  map d --> T
        (section4:but W is a low rank matrix, we note that the problem of learning a low-rank matrix factorization
        which approximates a given partially observed target matrix has been considered in[1][17] and references therein.)

        formulation: 2.2 unconstrained problem;  2.3 regularization error function;  2.4 optimizaion problem  2.5 convex optimization problem
    
    
U: feature vertors, maps the high dimension x_ti, to a low dimension space, regression parameter a_t. 
'''