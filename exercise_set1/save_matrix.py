
import numpy as np

# Create 15x15 matrix with random integers 0..9
matrix_c = np.random.default_rng().integers(10, size=(15, 15))

# Save matrix to file
np.savetxt('matrix.txt', matrix_c)