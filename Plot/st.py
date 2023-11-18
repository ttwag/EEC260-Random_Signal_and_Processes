import numpy as np
import matplotlib.pyplot as plt

# # Define the number of points for plotting
# num_points = 100
#
# # Generate random values for A
# A_values = np.random.uniform(0, 1, num_points)
#
# # Define values of t
# t_values = np.linspace(0, 1, num_points)
#
# # Compute X(t) for each value of t
# X_values = A_values**2 * t_values
#
# # Plot the stochastic process
# plt.plot(t_values, X_values, label=r'$X(t) = A^2 \cdot t$')
# plt.xlabel('t')
# plt.ylabel('X(t)')
# plt.title('Stochastic Process: $X(t) = A^2 \cdot t$ for Uniform(0, 1) A')
# plt.legend()
# plt.grid(True)
# plt.show()

A = np.array([[1, -1/3, -1/3, -1/3, 0, 0, 0],
              [-1/3, 1, 0, 0, -1/3, -1/3, 0],
              [-1/3, 0, 1, 0, -1/3, 0, -1/3],
              [-1/3, 0, 0, 1, 0, -1/3, -1/3],
              [0, -1/3, -1/3, 0, 1, 0, 0],
              [0, -1/3, 0, -1/3, 0, 1, 0],
              [0, 0, -1/3, -1/3, 0, 0, 1]])
b = np.array([0, 0, 0, 0, 1/3, 1/3, 1/3])
solution = (np.linalg.solve(A, b))
print(solution)
