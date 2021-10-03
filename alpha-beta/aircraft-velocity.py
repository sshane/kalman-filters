# Implemented from https://www.kalmanfilter.net/alphabeta.html

import matplotlib.pyplot as plt

# Estimates the future position of an aircraft using the State Etrapolation Equation
# Note that this assumes a constant aircraft velocity of 40 m/s

DELTA_T = 5  # seconds, radar track-to-track interval


class KalmanFilter:
  def __init__(self):
    # initialize the state estimates with known values
    self.x_hat = 30000  # predicted state of x (position in m)
    self.x_hat_d = 40  # the derivative of the state (just speed in m/s)

  def update(self):
    # Kalman - State extrapolation equation
    # Extrapolate position
    self.x_hat = self.x_hat + DELTA_T * self.x_hat_d

    # Extrapolate velocity (desired model assumes no change)
    self.x_hat_d = self.x_hat_d

  def predict(self, measurement):
    # Kalman - State update equation

    # The B and A gains are set manually depending on the known innacuracy/precision of the radar
    # B (for speed estimation) is set inversely proportional to the radar's measurement variance
    # A (for dist estimation) is set proportionally to the radar's measurement precision

    A = 0.2  # assume low radar precision, so use it less
    self.x_hat = self.x_hat + A * (measurement - self.x_hat)

    B = 0.1  # assume high radar variance, so use it less
    self.x_hat_d = self.x_hat_d + B * ((measurement - self.x_hat) / DELTA_T)


kf = KalmanFilter()

kf_estimates = []
measurements = [30110, 30265, 30740, 30750, 31135, 31015, 31180, 31610, 31865]  # from tutorial

for measurement in measurements:
  # Update state of system using described desired model
  # each update extrapolates the aircraft state out 5 seconds assuming 40 m/s constant velocity
  kf.update()
  kf.predict(measurement)
  kf_estimates.append(kf.x_hat)

plt.plot(kf_estimates, label='Kalman filter estimate')
plt.plot(measurements, label='Noisy measurements')
plt.legend()
