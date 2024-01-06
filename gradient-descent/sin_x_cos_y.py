import numpy as np
from matplotlib import pyplot as plt


def f(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """
    Represents f: R^2 -> R with f(x, y) = sin(x) + cos(y)
    """ 
    return np.sin(x) + np.cos(y)


def f_grad(x: np.ndarray, y: np.ndarray) -> tuple:
    """
    Represents f: R^2 -> R^2 with f'(x, y) = (cos(x), -sin(x))
    """
    grad_x = np.cos(x)
    grad_y = -np.sin(y)
    return grad_x, grad_y


def optimize_with_backtracking(x_0: float, y_0: float, beta: float, max_iterations: int, plot: bool):
    # Data for plotting. 
    x = np.linspace(-1, 1, 1000)
    y = np.linspace(-1, 1, 1000)
    
    # Create a meshgrid.
    X,Y = np.meshgrid(x,y)
    Z = f(X, Y)

    if plot:
        # Plotting setup
        plt.figure(num="f(x, y) = sin(x) + cos(y)") 
        plt.xlabel("x")
        plt.ylabel("y")
        plt.contour(X, Y, Z, cmap='viridis') 
        plt.colorbar(label='Function Value')    
        plt.show()


if __name__ == '__main__':
    optimize_with_backtracking(1, 1, 0.08, 100, True)
