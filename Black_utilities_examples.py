from Black_utilities import *
from Black_utilities.Black_utilities_self_contained_without_scipy import black_price_formula as sc_without_scipy_black_price_formula
from Black_utilities.Black_utilities_self_contained_without_scipy import black_implied_vol as sc_without_scipy_black_implied_vol

import timeit

F,K,T,sigma,isCall = 100,150,0.5,0.35,True
price = 0.0049011125057840665

def main():
    print("black_price_formula")
    print("-------------------")
    print("for: F = ", F, ", K = ", K, ", T = " , T, ", sigma = ", sigma, " , isCall = ", isCall, sep="")
    print("European option price using black_price_formula in cython =", round(black_price_formula(F,K,T,sigma,isCall),6))
    print(">>Performance analysis:")
    nb_loop = int(1e6)
    elapsed_time = timeit.timeit('black_price_formula(F,K,T,sigma,isCall)', 
                                 'from __main__ import black_price_formula, F,K,T,sigma,isCall', 
                                 number=nb_loop)  
    print(nb_loop, " pricing using black_price_formula in cython takes ", round(elapsed_time,4),"s.", sep="")
    nb_loop = int(1e3)
    elapsed_time = timeit.timeit('sc_without_scipy_black_price_formula(F,K,T,sigma,isCall)', 
                                 'from __main__ import sc_without_scipy_black_price_formula, F,K,T,sigma,isCall', 
                                 number=nb_loop)
    print(nb_loop, " pricing using black_price_formula in python (best direct implementation, without scipy) takes ", round(elapsed_time,4),"s.", sep="")

    print("black_implied_vol")
    print("-----------------")
    print("With the same parameters:")
    nb_loop = int(1e6)
    elapsed_time = timeit.timeit('black_implied_vol(price,F,K,T,isCall)', 
                                 'from __main__ import black_implied_vol, price,F,K,T,isCall', 
                                 number=nb_loop)  
    print(nb_loop, " implied vol computation using 'let's be rational' by Peter Jaeckel (accurate at 1e-15) in cython takes ", round(elapsed_time,4),"s.", sep="")
    nb_loop = int(1e3)
    elapsed_time = timeit.timeit('sc_without_scipy_black_implied_vol(price,F,K,T,isCall)', 
                                 'from __main__ import sc_without_scipy_black_implied_vol, price,F,K,T,isCall', 
                                 number=nb_loop)
    print(nb_loop, "  implied vol computation using Newton Raphson in python (best direct implementation, without scipy) with 1e-5 precision takes ", round(elapsed_time,4),"s.", sep="")   
    print("comment: we do not compare 'Let's be rational' by Peter Jaeckel with a C implementation of Newton Raphson.")
    print("Feel free to try it yourself, or read the article to understand why it is pointless.")

if __name__ == "__main__":
    main()