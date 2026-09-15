[![Open in GitHub Codespaces](
  https://img.shields.io/badge/Open%20in%20GitHub%20Codespaces-333?logo=github)](
  https://codespaces.new/dwave-training/iaqom-multi-vehicle-routing-disjointlist?quickstart=1)
  
# Multi-Vehicle Routing Problem With the Stride<sup>TM</sup> Hybrid Solver Using the Disjoint Lists Variable

For the multi-vehicle routing problem (MVRP), convert the mathematical formulation into a model in Python. Use disjoint lists to represent the decision variable and code the problem so it is compatible for submission to the Stride hybrid solver.

The objective is to minimize the total distance traveled by all vehicles. The decision variables represent the customer location(s) that each vehicle must visit and the order in which to visit them. There are two constraints: each customer (delivery) location must be visited exactly once by a single vehicle, and a vehicle cannot exceed its weight capacity.

Build the nonlinear model, define the objective function, and add the constraints.

The code in the repo is intended to help you answer the quiz questions in the online course and, thus, does not contain any `TODO` sections.

## Quiz: MVRP Distance Matrices

Explore code for the MVRP that creates a model object and defines the distance matrices.

Open and review `mvrp_distance_matrices.py` to answer the questions in the course quiz. This code:

   1. Imports the relevant packages.
   
   2. Creates a nonlinear model object called `model`.

   3. Defines the following constants matrices:
      - `full_dist_matrix`, where node `0` is the warehouse and nodes `1` to `5` are the customer locations.
      - `c_dist`, submatrix distance.
      - `w_dist`, submatrix distance.

## Quiz: MVRP Constants and Decision Variable

Continue working with MVRP code by examining more problem constants and defining the decision variable symbol.

Open and review `mvrp_constants_decision.py` to answer the questions in the course quiz. This code defines the following constants:

      - `customer_demand`, the demand of each customer location.
      - `num_customers`, the total number of customers.
      - `num_vehicles`, the total number of vehicles.
      - `vehicle_capacity`, the weight capacity of each vehicle.

## Quiz: MVRP Objective and Constraints

Continue coding the MVRP by examining the objective function and constraints.

Open and review `mvrp_objective_constraints.py` to answer the questions in the course quiz.
