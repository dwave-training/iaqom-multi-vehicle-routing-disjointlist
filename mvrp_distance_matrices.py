"""
A retail company needs to route two vehicles to five customer (delivery) locations. 
Assume that each vehicle starts from a single warehouse location and delivers 
resources to multiple delivery locations. All vehicles have the same weight capacity for how much cargo they can carry.

Objective: Minimize the total distance traveled by all vehicles.

Constraints:
Each customer (delivery) location must be visited exactly once by a single vehicle.
A vehicle cannot exceed its weight capacity.
"""

# Import the required packages.
import numpy as np
from dwave.optimization import Model

# Create the model.
# Initialize the nonlinear model.
model = Model()

# Define the constant matrices.
# Full distance matrix: node 0 is the warehouse and nodes 1 to 5 are the customer locations. 
full_dist_matrix = np.array(
    [
        [0, 4, 8, 2, 9, 1],
        [4, 0, 6, 1, 8, 5],
        [8, 6, 0, 3, 7, 3],
        [2, 1, 3, 0, 1, 6],
        [9, 8, 7, 1, 0, 8],
        [1, 5, 3, 6, 8, 0],
    ]
)

# Distance submatrices.
c_dist = full_dist_matrix[1:, 1:]         
w_dist = full_dist_matrix[0, 1:]            

