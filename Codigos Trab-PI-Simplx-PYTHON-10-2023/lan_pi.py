import numpy as np
from fklemint_pi_splx_norm import fkm_pi_splx_norm
from fklemint_pi_splx import fkm_pi_splx
from algpint_gf import algpint_01
import pandas as pd
import time

# Main part of the script
if __name__ == "__main__":
    # Clear variables and warnings
    from warnings import filterwarnings
    filterwarnings("ignore")
    cols=["dim","Iters","Tempo","ObjErro","SolutionErro","GAP"]
    row=list()
    dataFrame=pd.DataFrame(columns=cols)
    np.random.seed(42)

    # First call to the problem
    #print('  ------------------------------------------------------')
    #ndim = int(input('             Dimensão  do  espaço          =  '))
    #step=[0.01,0.05,0.10,0.30,0.50,0.70,0.80,0.90,0.95,0.99]
    dualGAP=[1e-1,1e-2,1e-4,1e-6,1e-8,1e-10]
    inputDim=[2,6,10,14,18,22,26]
    for actualGap in dualGAP:
        for ndim in inputDim:
                
            #print('  ------------------------------------------------------')

            # Construction of the optimization problem
            ncode = 1
            

            #print('  ------------------------------------------------------')
            #valb = float(input('      Define o vetor b (10 < valb < 100)   =  '))
            valb=25
            #print('  ------------------------------------------------------')
            start_time = time.time()
            A, B, C, REL, XMIN, XMAX = fkm_pi_splx(ndim, ncode, valb)

            # Calculated rank of matrix A
            IRANK, IR, IC = np.linalg.matrix_rank(A), None, None

            # Number of linearly independent rows
            if IRANK < len(XMIN):
                print('  ------------------------------------------------------------')
                print('     Rank (A) < dim. vet X . The problem is not consistent.   ')
                print('  ------------------------------------------------------------')
            else:
                # Define the first interior point near the origin
                Xini = (1.0e-11 + 1.0e-08 * np.random.rand(1)) * (XMAX / np.linalg.norm(XMAX))

                # Parameters for Interior Point
                gap = actualGap
                Maxiter = 20 * ndim
                KALPHA = 0.95

                iter, EVOLX, EVOLFOBJ, Xsol_pi, FOBJ, yk, gap_final = algpint_01(
                    A, B, C, REL, Xini, XMIN, XMAX, gap, KALPHA, Maxiter
                )
                end_time = time.time()

                execution_time = end_time - start_time

                Xsol = np.concatenate((np.zeros((ndim - 1)), [valb**(ndim-1)])).reshape(-1,1)
                print("Xsol ", Xsol)
                print("Xsol_pi ", Xsol_pi)
                print("FOBJ ", FOBJ)
                erro_xpi = 100 * np.linalg.norm(Xsol_pi - Xsol) / valb**(ndim - 1)
                erro_fobjpi = 100 * abs(FOBJ / (valb**(ndim - 1)) - 1)

                print('  ----------------------------------------------------------------  ')
                print(f'  Theoretical number of iterations for the simplex is = {2**ndim}')
                print(f'  PI number of iterations is                          = {iter}')
                print(f'  PI erro porcentual optimal objective value is       = {erro_fobjpi}')
                print(f'  PI erro porcentual vetor x soluçao                  = {erro_xpi}')
                print(f"Tempo de execução Pontos Interiores: {execution_time} segundos")
                print('  -----------------------------------------------------------------  ')
                row=[ndim,iter,execution_time,erro_fobjpi,erro_xpi,gap]
                dataFrame.loc[len(dataFrame)]=row
    
    name="DualGAP_PontosInteriores.csv"
    dataFrame.to_csv(path_or_buf=("C:\\Users\\Mediconchip\\Downloads\\Codigos-Trabalho PI-Simplx-01-2024\\Codigos-Trabalho PI-Simplx-01-2024\\PI_SIMPLEX_PYTHON\\Codigos Trab-PI-Simplx-PYTHON-10-2023\\ResultsPI\\"+name),sep=";",index=False)