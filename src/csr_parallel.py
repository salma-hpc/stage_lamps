import numpy as np
import time
from multiprocessing import Pool, cpu_count

def process_row(args):
    row_idx, row_data = args
    values = [val for val in row_data if val != 0]
    col_indices = [idx for idx, val in enumerate(row_data) if val != 0]
    return values, col_indices

def build_csr_parallel(dense_matrix, n_processes=None):
    if n_processes is None: n_processes = cpu_count()
    n_rows, n_cols = dense_matrix.shape
    
    with Pool(processes=n_processes) as pool:
        results = pool.map(process_row, [(i, dense_matrix[i, :]) for i in range(n_rows)])
    
    values, col_indices, row_ptr = [], [], [0]
    for vals, cols in results:
        values.extend(vals)
        col_indices.extend(cols)
        row_ptr.append(len(values))
        
    return np.array(values), np.array(col_indices), np.array(row_ptr)
