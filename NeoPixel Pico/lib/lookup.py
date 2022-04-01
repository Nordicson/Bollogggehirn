#Lookup Tables
import numpy as np

noise_arr = np.array([[0.51, 0.94, 0.45, 0.15, 0.46, 0.96, 0.53, 0.28, 0.22, 0.71, 0.04, 0.41, 0.63, 0.98, 0.31, 0.31, 0.29, 0.32, 1.0, 0.33, 0.53, 0.05, 0.88, 0.65, 0.58, 0.53, 0.29, 0.5, 0.21, 0.9, 0.94, 0.1, 0.58, 0.25, 0.88, 0.47, 0.0, 0.26, 0.13, 0.14, 0.87, 0.78, 0.09, 0.84, 0.25, 0.84, 0.88, 0.51, 0.44, 0.06, 0.51, 0.44, 0.07, 0.42, 0.01, 0.08, 0.39, 0.78, 0.02, 0.38, 0.67, 0.51, 0.9, 0.03, 0.69, 0.23, 0.06, 0.74, 0.07, 0.26],
     [0.88, 0.19, 0.34, 0.72, 0.95, 0.11, 0.21, 0.21, 0.31, 0.41, 0.9, 0.56, 0.28, 0.67, 0.82, 0.97, 0.05, 0.56, 0.36, 0.39, 0.31, 0.81, 0.84, 0.64, 0.11, 0.2, 0.3, 0.77, 0.74, 0.63, 0.91, 0.59, 0.18, 0.21, 0.76, 0.26, 0.77, 0.01, 0.99, 0.89, 0.83, 0.6, 0.37, 0.86, 0.56, 0.9, 0.09, 0.23, 0.32, 0.49, 0.12, 0.41, 0.06, 0.49, 0.16, 0.11, 0.24, 0.45, 0.96, 0.18, 0.44, 0.36, 0.34, 0.35, 0.29, 0.48, 0.03, 0.75, 0.33, 0.84],
     [0.86, 0.94, 0.4, 0.4, 0.96, 0.8, 0.91, 0.13, 0.29, 0.2, 0.35, 0.93, 0.85, 0.38, 0.95, 0.97, 0.36, 0.49, 0.9, 0.76, 0.25, 0.12, 0.58, 0.53, 0.65, 0.46, 0.77, 0.73, 0.0, 0.53, 0.81, 0.08, 0.91, 0.74, 0.92, 0.35, 0.12, 0.21, 0.35, 0.54, 0.26, 0.26, 0.33, 0.66, 0.45, 0.92, 0.05, 0.86, 0.89, 0.65, 0.67, 0.86, 0.08, 0.85, 0.33, 0.7, 0.2, 0.47, 0.69, 0.79, 0.03, 0.84, 0.28, 0.55, 0.45, 0.05, 0.18, 0.71, 0.92, 0.95],
     [0.08, 0.85, 0.15, 0.65, 0.92, 0.39, 0.06, 0.35, 0.66, 0.04, 0.11, 0.84, 0.87, 0.48, 0.16, 0.73, 0.93, 0.2, 0.79, 0.28, 0.62, 0.49, 0.43, 0.25, 0.52, 0.77, 0.98, 0.85, 0.74, 0.2, 0.86, 0.04, 0.14, 0.94, 0.07, 0.09, 0.39, 0.46, 0.01, 0.15, 0.39, 0.71, 0.15, 0.57, 0.25, 0.06, 0.25, 0.9, 0.13, 0.37, 0.48, 0.69, 0.88, 0.1, 0.12, 0.4, 0.03, 0.54, 0.0, 0.63, 0.94, 0.93, 0.91, 0.06, 0.81, 0.83, 0.06, 0.62, 0.48, 0.6],
     [0.38, 0.37, 0.45, 0.73, 0.33, 0.59, 0.41, 0.46, 0.47, 0.05, 0.56, 0.06, 0.23, 0.5, 0.53, 0.43, 0.68, 0.87, 1.0, 0.71, 0.51, 0.36, 0.27, 0.71, 0.59, 0.79, 0.84, 0.48, 0.76, 0.29, 0.31, 0.78, 0.54, 0.99, 0.72, 0.52, 0.37, 0.35, 0.34, 0.16, 0.37, 0.51, 0.97, 0.79, 0.77, 0.45, 0.78, 0.99, 0.37, 0.43, 0.56, 0.35, 0.03, 0.74, 0.44, 0.15, 0.92, 0.57, 0.74, 0.29, 0.31, 0.5, 0.13, 0.81, 0.18, 0.32, 0.35, 0.06, 0.07, 0.06]
     ])

def noise(number):
    return noise_arr[number]

print(noise(1))