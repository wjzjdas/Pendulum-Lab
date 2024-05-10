import matplotlib.pyplot as plt
import numpy as np

# Data
lengths = np.array([10.0, 15.0, 20.0, 25.0, 30.0])  # in cm
periods = np.array([0.80, 1.00, 1.13, 1.22, 1.35])  # in radian
length_uncertainty = 0.3  # in cm
period_uncertainty = 0.03  # in radian

# Calculate log values
log_lengths = np.log10(lengths)
log_periods = np.log10(periods)

# Calculate error bars in log scale
log_length_error = length_uncertainty / (lengths * np.log(10))
log_period_error = period_uncertainty / (periods * np.log(10))

# Fit a straight line to the data
fit_params = np.polyfit(log_lengths, log_periods, 1)
fit_line = np.poly1d(fit_params)

# Plotting with smaller data points
plt.errorbar(log_lengths, log_periods, xerr=log_length_error, yerr=log_period_error, fmt='o', color='black', markersize=5, label='Data')
plt.plot(log_lengths, fit_line(log_lengths), '-k', label='Line of Best Fit')

# Add labels and title
plt.xlabel('Log(Length of Pendulum) (cm)')
plt.ylabel('Log(Period of Pendulum) (radian)')
plt.title('Log-Log Plot: Period of Pendulum vs Length of Pendulum')

# Remove gridlines
plt.grid(False)

# Show the plot
plt.legend()
plt.show()
