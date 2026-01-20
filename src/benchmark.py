import numpy as np
import time
from csr_matrix import CSRMatrix
from csr_parallel import build_csr_parallel

def run_benchmarks():
    sizes = [1000, 2000]
    print(f"{'Taille':<10} {'Seq (s)':<10} {'Par (s)':<10} {'Gain'}")
    print("-" * 40)
    
    for size in sizes:
        # Génération matrice sparse (1% densité)
        matrix = np.random.choice([0, 1], size=(size, size), p=[0.99, 0.01])
        
        start = time.time()
        CSRMatrix.from_dense(matrix)
        t_seq = time.time() - start
        
        start = time.time()
        build_csr_parallel(matrix)
        t_par = time.time() - start
        
        print(f"{size:<10} {t_seq:<10.2f} {t_par:<10.2f} x{t_seq/t_par:.2f}")

if __name__ == "__main__":
    run_benchmarks()
