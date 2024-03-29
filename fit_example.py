# Sample Python code to run the fit_black_box Python code relatively easily

import fit_black_box as bb
import numpy as np

# First, define the function you want to fit. Here it's a linear function.
# It is critical that the independant variable ("t") is first in the list of function variables.

def linear(t, m, b):
    return m*t + b

# Next, generate your data and errorbars. One way is to manually insert it here.

x = bb.np.array([1,1,1])
y = bb.np.array([1,1,1])
xerr = 0.05
yerr = 0.001

# Note that xerr and yerr can either be an array of the same length as x&y, or a single value
"""
def exponential(x,a,b,c):
    return a*np.exp(b*x)

# Now we make the plot, displayed on screen and saved in the directory, and print the best fit values

bb.plot_fit(linear, x, y, xerr, yerr)

# Let's try again, this time loading from a file like a CSV file.
# NOTE: The CSV file should not have commas to separate things! Spaces or tabs are fine.

# Again, start with a fitting function. This time it is quadratic.
"""
def quadratic(t, a, b, c):
    return a*t**2 + b*t + c

# Now load the data from the file. The file should be in the same directory as this Python code.
# Some chance you will need an absolute path: "C:\\Users\\Brian\\Python\\mydata_fake.txt"

filename="pendulum_length.txt"
x, y, xerr, yerr = bb.load_data(filename)

# This time, let's use every single possible option available to bb.plot_fit()

init_guess = (-0.50, 0, +0.50) # guess for the best fit parameters
font_size = 12
xlabel = "Length (cm)"
ylabel = "Q Factor"

# Now we make the plot, displayed on screen and saved in the directory, and print the best fit values
bb.plot_fit(quadratic, x, y, xerr, yerr, init_guess=init_guess, font_size=font_size,
            xlabel=xlabel, ylabel=ylabel)

# Note: for sinusoidal functions, guessing the period correctly with init_guess is critical

