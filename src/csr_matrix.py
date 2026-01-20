import numpy as np
import time

class CSRMatrix:
    def __init__(self, values, col_indices, row_ptr, shape):
        self.values = np.array(values)
        self.col_indices = np.array(col_indices)
        self.row_ptr = np.array(row_ptr)
        self.shape = shape
    
    @classmethod
    def from_dense(cls, dense_matrix):
        start_time = time.time()
        n_rows, n_cols = dense_matrix.shape
        values = []
        col_indices = []
        row_ptr = [0]
        
        for i in range(n_rows):
            for j in range(n_cols):
                if dense_matrix[i, j] != 0:
                    values.append(dense_matrix[i, j])
                    col_indices.append(j)
            row_ptr.append(len(values))
        
        return cls(values, col_indices, row_ptr, (n_rows, n_cols))

    def memory_usage(self):
        csr_mem = len(self.values) + len(self.col_indices) + len(self.row_ptr)
        dense_mem = self.shape[0] * self.shape[1]
        reduction = (1 - csr_mem / dense_mem) * 100
        return csr_mem, dense_mem, reduction
