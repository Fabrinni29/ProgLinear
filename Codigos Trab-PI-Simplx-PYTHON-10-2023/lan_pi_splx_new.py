import numpy as np
from revised_simplex import revised_simplex
from Murtyalgorithm import Murtyalgorithm_05
from otcrank import otcrank
from algpint_gf import algpint_01
from fklemint_pi_splx import fkm_pi_splx
from numpy.linalg import matrix_rank
import time
import pandas as pd


# Setting the precision to long format
np.set_printoptions(precision=15)

# Turn off warnings about singular or badly scaled matrices
#2np.warnings.filterwarnings("ignore")
cols=["dim","Iters","Tempo","GAP"]
row=list()
dataFrame=pd.DataFrame(columns=cols)
# Input for the dimension of the space
#print('  ------------------------------------------------------')
#ndim = int(input('               Dimensao  do  espaco         =  '))
#print('  ------------------------------------------------------')
dualGAP=[1e-1,1e-2,1e-4,1e-6,1e-8,1e-10]
inputDim=[2,6,10,14,18,22,26]
for actualGap in dualGAP:
    for ndim in inputDim:
        # Construction of the optimization problem
        ncode = 1

        #print('  ------------------------------------------------------')
        #valb = float(input('      Define o vetor b (10 < valb < 100)   =  '))
        valb=25
        #print('  ------------------------------------------------------')
        start_time = time.time()

        # Construct the problem using the fklemint_pi_splx function
        A, B, C, REL, XMIN, XMAX = fkm_pi_splx(ndim, ncode, valb)

        # Calculate the rank of matrix A
        #IRANK, _, _ = otcrank(A)
        IRANK = matrix_rank(A)
        print("rank: ", IRANK)
        # Check if the rank condition is met
        if IRANK < len(XMIN):
            print('  ---------------------------------------------------------')
            print('    Rank (A) < dim. vet X. The problem is not consistent. ')
            print('  ---------------------------------------------------------')
        else:
            # Define the specified value considered as zero
            valzero = np.sqrt(np.finfo(float).eps)**3

            # Define the first interior point near the origin
            #Xini = (np.finfo(float).eps + np.finfo(float).eps * np.random.rand(1)) * (XMAX / np.linalg.norm(XMAX))
            Xini=(1.0e-11 + 1.0e-08 * np.random.rand(1)) * (XMAX / np.linalg.norm(XMAX))
            # Parameters for the Interior Point algorithm
            gap = actualGap
            Maxiter = 20 * ndim
            KALPHA = 0.95

            # Call the algpint_01 function to solve the problem
            ITER, EVOLX, EVOLFOBJ, Xsol_pi, FOBJ, yk, gap_final = algpint_01(A, B, C, REL, Xini, XMIN, XMAX, gap, KALPHA, Maxiter)

            # Calculate errors
            Xsol = np.concatenate((np.zeros((ndim - 1, 1)), valb**(np.arange(ndim - 1, dtype=float)).reshape(-1, 1)))
            Xsol_pi[ndim - 1] = Xsol_pi[ndim - 1] - valb**(ndim - 1)
            erro_xpi = 100 * np.linalg.norm(Xsol_pi) / valb**(ndim - 1)
            Xsol_pi[ndim - 1] = Xsol_pi[ndim - 1] + valb**(ndim - 1)
            erro_fobjpi = 100 * abs(FOBJ - valb**(ndim - 1)) / valb**(ndim - 1)

            # Display results
            print('  ---------------------------------------------------------  ')
            print(f'    Pi number of iterations is                      = {ITER}')
            print(f'    Pi erro porcentual  optimal objective value is  = {erro_fobjpi}')
            print(f'    Pi erro porcentual vetor x solucao              = {erro_xpi}')
            print('  ---------------------------------------------------------  ')

            print('  ')
            print('  -------------------------------------------------  ')
            print('     Utilizando o metodo de Murty : Amanda & Igor     ')
            print('  -------------------------------------------------  ')
            print('  ')

            # Run the Murtyalgorithm to solve the problem
            ncode = 2
            As, bs, cs, REL, XMIN, XMAX = fkm_pi_splx(ndim, ncode, valb)
            _, FBS = Murtyalgorithm_05(As, -cs.T, yk)

            # Define epsilon
            eps11 = 1e-6

            # Call the revised_simplex_01 function to solve the problem
            obj, x, y, iter_spx, evolx, xb1, B = revised_simplex(cs, As, bs, eps11, FBS)
            print(iter_spx)
            Xsol_splx = x[:ndim]
            Xsol_splx[ndim - 1] = Xsol_splx[ndim - 1] - valb**(ndim - 1)
            end_time = time.time()

            execution_time = end_time - start_time
            print("Xsol ", Xsol)
            print("Xsol Simplex ", x)
            print("FOBJ ", obj)
            erro_xsplx = 100 * np.linalg.norm(Xsol_splx) / valb**(ndim - 1)
            erro_fobjsplx = 100 * abs(obj - valb**(ndim - 1)) / valb**(ndim - 1)

            # Display results
            print('  -------------------------------------------------------------------  ')
            print(f'    Theoretical number of iterations for the simplex is  = {2 ** ndim}')
            print(f'    Pi number of iterations is                           = {ITER}')
            print(f'    Simplex number of iterations is                      = {iter_spx}')
            print(f'    Simplex erro porcentual optimal objective value is   = {erro_fobjsplx}')
            print(f'    Simplex erro porcentual vetor x solucao              = {erro_xsplx}')
            print(f"Tempo de execução Pontos Interiores Hibrido Simplex: {execution_time} segundos")

            print('  -------------------------------------------------------------------  ')

            row=[ndim,iter_spx+ITER,execution_time,gap]
            dataFrame.loc[len(dataFrame)]=row
    
name="DualGapHibrido.csv"
dataFrame.to_csv(path_or_buf=("C:\\Users\\Mediconchip\\Downloads\\Codigos-Trabalho PI-Simplx-01-2024\\Codigos-Trabalho PI-Simplx-01-2024\\PI_SIMPLEX_PYTHON\\Codigos Trab-PI-Simplx-PYTHON-10-2023\\ResultsPI\\"+name),sep=";",index=False)