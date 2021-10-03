# Implemented from https://www.kalmanfilter.net/alphabeta.html

import matplotlib.pyplot as plt
import numpy as np

# Stateless estimation of a static system;
# weight of gold bars given measurements with low precision (no measurement bias)

x = 1010  # true value of the gold bars (in any unit)


class KalmanFilter:
  def __init__(self):
    self.x_hat = 0  # predicted state of x
    self.N = 0  # how many measurements we've been given

  @property
  def Kn(self):
    # Also known as the Kalman Gain, Kn
    return 1 / self.N

  def predict(self, measurement):
    # Kalman - State update equation
    self.N += 1
    self.x_hat = self.x_hat + self.Kn * (measurement - self.x_hat)
    return self.x_hat


kf = KalmanFilter()

kf_estimates = []
measurements = []

for _ in range(20):
  # crappy scale, has standard deviation of 4 (affects measurement precision, not bias)
  measurements.append(measurement := np.random.normal(x, 10))
  kf_estimates.append(kf.predict(measurement))
  print('Measurement: {}, estimated weight of gold bars: {}'.format(measurement, kf.x_hat))

plt.plot(kf_estimates, label='Kalman filter estimate')
plt.plot(measurements, label='Noisy measurements')
plt.plot([x] * len(measurements), label='Real value')
plt.legend()
