[![Open in GitHub Codespaces](
  https://img.shields.io/badge/Open%20in%20GitHub%20Codespaces-333?logo=github)](
  https://codespaces.new/dwave-training/iaqom-multi-vehicle-routing-disjointlist?quickstart=1)
  
# Multi-Vehicle Routing Problem With the Stride<sup>TM</sup> Hybrid Solver Using the Disjoint Lists Variable

For the multi-vehicle routing problem (MVRP), convert the mathematical formulation into a model in Python. Use disjoint lists to represent the decision variable and code the problem so it is compatible for submission to the Stride hybrid solver.

The objective is to minimize the total distance traveled by all vehicles. The decision variables represent the customer location(s) that each vehicle must visit and the order in which to visit them. There are two constraints: each customer (delivery) location must be visited exactly once by a single vehicle, and a vehicle cannot exceed its weight capacity.

Build the nonlinear model, define the objective function, and add the constraints.

The code in the repo is intended to help you answer the quiz questions in the online course and, thus, does not contain any `TODO` sections.

## Quiz: MVRP Distance Matrices

In the quiz MVRP Distance Matrices, create the model object and define the constant matrices.

Open `mvrp_distance_matrices.py`.

   1. Import the relevant packages.
   
   2. Create a nonlinear model object called `model`.

   3. Define the following constants matrices:
      - `full_dist_matrix`, where node `0` is the warehouse and nodes `1` to `5` are the customer locations.
      - `c_dist`, submatrix distance.
      - `w_dist`, submatrix distance.

## Quiz: MVRP Constants and Decision Variable

In the quiz MVRP Constants and Decision Variable, define additional constants.

Start with the work completed in the MVRP Distance Matrices quiz. Create the model object, define the constants matrices, and then add additional constants.

Open `mvrp_constants_decision.py`.

   1. Copy all the work completed in the code file `mvrp_distance_matrices.py`.
   
   2. Define the following constants:
      - `customer_demand`, the demand of each customer location.
      - `num_customers`, the total number of customers.
      - `num_vehicles`, the total number of vehicles.
      - `vehicle_capacity`, the weight capacity of each vehicle.

## Quiz: MVRP Objective and Constraints

In the quiz MVRP Objective and Constraints, add the constants to the model object, create the decision variable, build the objective function, and add the constraints.

Start with the work completed in the quiz MVRP Constants and Decision Variable. Create the model object, define the constant matrices, add the constants (from quiz 2), and then add those constants to the model object. Next, create the disjoint lists to represent the decision variable. Finally, build the objective function and add the constraints.

Formulate the problem so that it is compatible for submission to the Stride Hybrid solver, but do not submit it to the solver yet.

Open the code file `mvrp_objective_constraints.py`.

   1. Copy all the work completed in the code file `mvrp_constants_decision.py`.
    
   2. Add the constants to the model object.

   3. Create the disjoint lists as the decison variable.

   4. Build the objective function:
      - Add the constraint that each vehicle cannot exceed its weight capacity.
      - Set the objective function to minimize the total distance traveled by all vehicles.
