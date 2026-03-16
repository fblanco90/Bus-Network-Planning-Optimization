# Bus Network Planning Optimization (TFG)

## Overview
This repository contains the source code and data for the Bachelor's Thesis **"Optimization of Public Transport Networks"**, developed at the *Universidad de Sevilla* (2024).

The project focuses on optimizing urban bus networks using mathematical programming (MILP). It addresses the problem from two distinct perspectives:
1.  **Passenger Perspective:** Minimizing total travel time (waiting, in-vehicle, transfer, and walking time).
2.  **Operator Perspective:** Maximizing network profitability (revenue vs. operational costs).

The model is applied to the **Mandl's Swiss Network (1980)**, a benchmark instance in transit network design.

## Features
* **Iterative Design Model:** Generates bus lines, frequencies, and fleet sizes.
* **Bimodal Graph:** Integrates bus and pedestrian layers to allow realistic transfers and walking options.
* **Gurobi Optimization:** Uses the Gurobi Optimizer to solve complex Mixed-Integer Linear Programming (MILP) formulations.
* **Scenario Analysis:** Capable of running multiple scenarios varying in maximum lines, fleet size, and frequencies.
* **Visualization:** Outputs results to Excel and generates network graphs.

## Prerequisites
* Python 3.8+
* **Gurobi Optimizer** (Requires a valid license, e.g., Academic or Web License).

## Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/your-username/bus-network-optimization.git](https://github.com/fblanco90/bus-network-planning-optimization.git)
    cd bus-network-optimization
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Setup Data**
    Ensure all input text files (`Stops_Mandl.txt`, `OD_Mandl.txt`, etc.) are located in the `data/` directory.

## Usage
Run the main iterative model:

```bash
python src/main_model.py
