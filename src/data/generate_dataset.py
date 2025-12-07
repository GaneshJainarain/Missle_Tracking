import numpy as np
import pandas as pd
from pathlib import Path

# -----------------------------
# Output Path
# -----------------------------
OUTPUT_PATH = Path("data/raw/chase_dataset_raw.csv")
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Simulation Parameters
# -----------------------------
dt = 0.1                # Time step (seconds)
total_time = 120.0      # Total simulation time (seconds)
num_steps = int(total_time / dt)

interception_threshold = 5.0

# -----------------------------
# Initial Target State
# -----------------------------
target_position = np.array([0.0, 0.0, 500.0])
target_velocity = np.array([40.0, 5.0, 0.5])

# -----------------------------
# Initial Chaser State
# -----------------------------
chaser_position = np.array([-500.0, -3000.0, 0.0])
chaser_velocity = np.array([150.0, 120.0, 10.0])

# -----------------------------
# Storage
# -----------------------------
rows = []

# -----------------------------
# Simulation Loop
# -----------------------------
for step in range(num_steps):

    time_seconds = step * dt

    # Relative Geometry
    relative_position = target_position - chaser_position
    distance_between = np.linalg.norm(relative_position) + 1e-6
    relative_velocity = target_velocity - chaser_velocity

    # Log Current State
    rows.append({
        "time_seconds": time_seconds,

        # Target State
        "target_position_x": target_position[0],
        "target_position_y": target_position[1],
        "target_position_z": target_position[2],
        "target_velocity_x": target_velocity[0],
        "target_velocity_y": target_velocity[1],
        "target_velocity_z": target_velocity[2],

        # Chaser State
        "chaser_position_x": chaser_position[0],
        "chaser_position_y": chaser_position[1],
        "chaser_position_z": chaser_position[2],
        "chaser_velocity_x": chaser_velocity[0],
        "chaser_velocity_y": chaser_velocity[1],
        "chaser_velocity_z": chaser_velocity[2],

        # Relative Geometry
        "relative_position_x": relative_position[0],
        "relative_position_y": relative_position[1],
        "relative_position_z": relative_position[2],
        "relative_velocity_x": relative_velocity[0],
        "relative_velocity_y": relative_velocity[1],
        "relative_velocity_z": relative_velocity[2],
        "distance_between": distance_between,
    })

    # -----------------------------
    # Physics-Based Pursuit Update (Teacher Policy)
    # -----------------------------
    direction_unit = relative_position / distance_between

    acceleration = 8.0 * direction_unit
    chaser_velocity = chaser_velocity + acceleration * dt

    # Velocity Clipping
    max_speed = 400.0
    speed = np.linalg.norm(chaser_velocity)
    if speed > max_speed:
        chaser_velocity *= max_speed / speed

    chaser_position = chaser_position + chaser_velocity * dt

    # -----------------------------
    # Target Motion Update (Curved Path)
    # -----------------------------
    target_velocity = target_velocity + np.array([0.0, 0.02, 0.01])
    target_position = target_position + target_velocity * dt

    # Optional: Stop once intercepted
    if distance_between <= interception_threshold:
        print(f"Intercept achieved at step {step}")
        break

# -----------------------------
# Build DataFrame
# -----------------------------
df = pd.DataFrame(rows)

# -----------------------------
# Add Supervised Labels (Next Chaser Position)
# -----------------------------
df["next_chaser_position_x"] = df["chaser_position_x"].shift(-1)
df["next_chaser_position_y"] = df["chaser_position_y"].shift(-1)
df["next_chaser_position_z"] = df["chaser_position_z"].shift(-1)

# Drop final row (no next state)
df = df.iloc[:-1].reset_index(drop=True)

# -----------------------------
# Save Dataset
# -----------------------------
df.to_csv(OUTPUT_PATH, index=False)

print("Dataset successfully generated.")
print("Shape:", df.shape)
print("Saved to:", "/Users/ganeshjai/Documents/Missle_Tracking/data/external")
