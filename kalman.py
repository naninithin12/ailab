import numpy as np

def kalman_filter(measurements):
    # Kalman Filter parameters
    dt = 1.0  # time step
    A = np.array([[1, dt], [0, 1]])  # state transition matrix
    H = np.array([[1, 0]])  # observation matrix
    Q = np.array([[0.01, 0], [0, 0.01]])  # process noise covariance
    R = np.array([[0.1]])  # measurement noise covariance

    # Initial state
    x = np.array([[0], [0]])  # position and velocity
    P = np.array([[0, 0], [0, 0]])  # state covariance

    # Estimated position and velocity lists
    positions = []
    velocities = []

    # Kalman Filter loop
    for measurement in measurements:
        # Prediction
        x = np.dot(A, x)
        P = np.dot(np.dot(A, P), A.T) + Q

        # Update
        y = measurement - np.dot(H, x)
        S = np.dot(np.dot(H, P), H.T) + R
        K = np.dot(np.dot(P, H.T), np.linalg.inv(S))
        x = x + np.dot(K, y)
        P = np.dot((np.eye(2) - np.dot(K, H)), P)

        # Append position and velocity to the lists
        positions.append(x[0][0])
        velocities.append(x[1][0])

    return positions, velocities
measurements = [1.0, 100.0, 129.0]  # example measurements

positions, velocities = kalman_filter(measurements)

# Print position and velocity at each time step
for i in range(len(positions)):
    print("Time Step:", i)
    print("Position:", positions[i])
    print("Velocity:", velocities[i])
    print("-------------------------")
