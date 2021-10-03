from tools.filter_simple import FirstOrderFilter
import matplotlib.pyplot as plt
import numpy as np

# Stateless estimation of a static model;
# weight of gold bars given measurements with low precision (no measurement bias)

x = 15  # true value of the gold bars (in any unit)


class KalmanFilter:
  def __init__(self):
    self.x_hat = 0  # predicted state of x
    self.N = 0  # how many measurements we've been given

  def update(self, measurement):
    # Kalman - State update equation
    self.N += 1
    self.x_hat = self.x_hat + 1 / self.N * (measurement - self.x_hat)
    return self.x_hat


kf = KalmanFilter()

kf_estimates = []
measurements = []

for _ in range(20):
  # crappy scale, has standard deviation of 4 (affects measurement precision, not bias)
  measurements.append(measurement := np.random.normal(x, 3))
  kf_estimates.append(kf.update(measurement))
  print('Measurement: {}, estimated weight of gold bars: {}'.format(measurement, kf.x_hat))

plt.plot(kf_estimates, label='Kalman filter estimate')
plt.plot(measurements, label='Noisy measurements')
plt.plot([x] * len(measurements), label='Real value')
plt.legend()
