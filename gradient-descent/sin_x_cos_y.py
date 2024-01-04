import numpy
from matplotlib import pyplot as plt


def f(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """
    Represents f: R^2 -> R with f(x, y) = sin(x) + cos(y)
    """ 
    return np.sin(x) + np.cos(y)


def f_grad(x: np.ndarray, y: np.ndarray) -> np.ndarray, np.ndarray:
    """ 
    Represents f: R^2 -> R^2 with f'(x, y) = (cos(x), -sin(x))
    """ 
    grad_x = np.cos(x)
    grad_y = -np.sin(y)
    return grad_x, grad_y


def optimizer_with_backtracking(x_0: float, beta: float, max_iterations: int, plot: bool):
    pass


if __name__ == '__main__':
    pass
