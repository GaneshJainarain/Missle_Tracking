# Chaser ML: A 3D Pursuit and Interception Machine Learning System

This project is a full end-to-end machine learning control system that
learns how to guide a chaser agent in 3D space to intercept a moving
target. The system integrates:

-   Synthetic trajectory generation\
-   Classical machine learning and neural networks\
-   Real-time 3D simulation\
-   MLflow experiment tracking\
-   DVC dataset versioning\
-   FastAPI model inference\
-   Streamlit web UI\
-   Dockerized deployment

This project is a purely academic simulation. The "target" and "chaser"
are abstract 3D agents represented as points in space.\
There is no real-world weapon modeling, no radar modeling, no
aerodynamics, and no military system replication.\
The project exists strictly as a machine learning and control systems
learning environment.

------------------------------------------------------------------------

## Conceptual Inspiration (Academic Only)

This project is conceptually inspired by traditional guidance and
control literature such as:

-   *Missile Guidance and Control Systems* (theoretical closed-loop
    control systems)
-   *STANDARD Missile Guidance System Development* (multi-phase guidance
    concepts)

No real engineering designs, hardware logic, or operational systems from
these texts are implemented.\
They serve only as high-level theoretical motivation for:

-   Closed-loop control\
-   Target pursuit dynamics\
-   Interception logic\
-   State-based predictive control

------------------------------------------------------------------------

## Problem Definition

At each time step `t`, the system observes the full 3D state of:

### Target Agent

    (target_position_x, target_position_y, target_position_z)
    (target_velocity_x, target_velocity_y, target_velocity_z)

### Chaser Agent

    (chaser_position_x, chaser_position_y, chaser_position_z)
    (chaser_velocity_x, chaser_velocity_y, chaser_velocity_z)

The machine learning model predicts the next chaser position:

    (next_chaser_position_x,
     next_chaser_position_y,
     next_chaser_position_z)

The simulation continues until the Euclidean distance satisfies:

    || target_position - chaser_position || ≤ interception_threshold

This creates a closed-loop predictive control system where the model's
output directly affects the next physical state.

------------------------------------------------------------------------

## Dataset Design

Each dataset row represents one time step and contains:

### Inputs (Features)

-   `time_seconds`

Target State\
- `target_position_x`, `target_position_y`, `target_position_z`\
- `target_velocity_x`, `target_velocity_y`, `target_velocity_z`

Chaser State\
- `chaser_position_x`, `chaser_position_y`, `chaser_position_z`\
- `chaser_velocity_x`, `chaser_velocity_y`, `chaser_velocity_z`

Relative Geometry\
- `relative_position_x`, `relative_position_y`, `relative_position_z`\
- `relative_velocity_x`, `relative_velocity_y`, `relative_velocity_z`\
- `distance_between`

### Output (Label)

-   `next_chaser_position_x`\
-   `next_chaser_position_y`\
-   `next_chaser_position_z`

The dataset is generated entirely via synthetic physics-based pursuit
simulation.

------------------------------------------------------------------------

## Machine Learning Strategy

The project is structured in three modeling phases:

### Phase 1 --- Baseline Models

-   Linear Regression\
-   Random Forest Regressor\
-   Gradient Boosted Trees (planned)

### Phase 2 --- Neural Networks

-   Fully Connected MLP\
-   Sequence Models (LSTM/GRU) for temporal prediction

### Phase 3 --- Reinforcement Learning (Future)

-   State → Action → Reward control formulation

All experiments are tracked with MLflow.

------------------------------------------------------------------------

## 3D Simulation Engine

The simulation is built using:

-   matplotlib\
-   FuncAnimation\
-   Axes3D

Features: - Real-time 3D motion\
- Target trajectory visualization\
- Chaser pursuit trajectory\
- Distance-to-target display\
- Automatic termination upon interception

Two simulation modes: - Physics-driven control\
- Machine learning-driven control

------------------------------------------------------------------------

## MLOps Stack

  Tool        Purpose
  ----------- ---------------------------
  DVC         Dataset versioning
  MLflow      Experiment tracking
  Docker      Reproducible environments
  FastAPI     Model inference service
  Streamlit   Interactive control UI

------------------------------------------------------------------------

## FastAPI Inference API

The trained model is served via a REST API:

    POST /predict

Input: - Current target state\
- Current chaser state\
- Relative geometry

Output:

    {
      "next_chaser_position_x": float,
      "next_chaser_position_y": float,
      "next_chaser_position_z": float
    }

------------------------------------------------------------------------

## Streamlit Web UI

The web interface allows: - Manual input of target and chaser state\
- Live machine learning inference via FastAPI\
- Visual inspection of the next predicted chaser motion

------------------------------------------------------------------------

## Dockerized Deployment

The full stack is runnable via:

    docker compose up --build

This launches: - FastAPI inference server\
- Streamlit UI frontend

------------------------------------------------------------------------

## Project Structure

    chaser-ml-project/
    ├── data/
    ├── models/
    ├── src/
    │   ├── data/
    │   ├── models/
    │   ├── simulation/
    │   └── utils/
    ├── api/
    ├── ui/
    ├── notebooks/
    ├── dvc.yaml
    ├── Dockerfile
    ├── docker-compose.yml
    └── README.md

------------------------------------------------------------------------

## Project Goals

-   Learn closed-loop predictive control with machine learning\
-   Explore physics-driven versus ML-driven pursuit\
-   Practice full MLOps workflows\
-   Build real-time ML simulations\
-   Create a portfolio-grade machine learning systems project

------------------------------------------------------------------------

## Ethical Disclaimer

This project: - Does not model real weapons\
- Does not simulate real sensors\
- Does not implement real guidance hardware\
- Does not support real-world deployment

It exists solely for: - Machine learning education\
- Control systems learning\
- Simulation and visualization practice\
- ML systems engineering

------------------------------------------------------------------------

## Status

-   Dataset generator implemented\
-   Baseline ML implemented\
-   Random Forest implemented\
-   3D simulation implemented\
-   FastAPI inference implemented\
-   Streamlit UI implemented\
-   Docker implemented\
-   Neural Network controller planned\
-   Reinforcement learning agent planned

------------------------------------------------------------------------
