# some-optimization-algorithms

## Algorithms
- Gradient descent
- Gauss-Newton algorithm
- Conjugate gradient method

### Gradient descent
Gradient descent is an iterativ Algorithm to find a local optimum (minimum) of a differentiable multivariate function.

Let $f \in C^{1}$ (at least one time differentiable). The gradient of f, f' = grad f = ($\displaystyle \frac{\partial f}{\partial x_{1}}$, $\displaystyle \frac{\partial f}{\partial x_{2}}$, ..., $\displaystyle \frac{\partial f}{\partial x_{n}}$)^T (T for transpose).

#### Iterative Method

$x^{k + 1}$ = $x^{k}$ - $\tau^{k}$ grad f($x^{k}$)

with an startvalue $x^{0}$.

The stepsize $\tau^{k}$ should be chosen optimal, that the following condition is satisfied:

f($x^k$ - $\tau^k$ grad f($x^k$) $\leq$ f($x^k$ - $\epsilon$ grad f($x^k$) $\forall$ $\epsilon$ $\geq$ 0

#### Wolfe conditions to find the best $\tau$

#### Armijo rule and backtracking line search

f($x^k$ - $\tau^k$ grad f($x^k$) - f($x^k$) $\leq$ $\delta$ $\tau$ grad f($x^k$)^T (- grad f($x^k$)

with $\delta \in (0, 1)$ and usually $\delta$ = 10e-4.

##### Example:

```js
beta = 0.9
delta = 10e-4
while f(x_k - tau * f_grad(x_k)) - f(x_k) > delta * tau * f_grad(x_k).T * (-f_grad(x_k)):
  tau = beta * tau
```

### Newtons method
Newtons method is and iterativ Algorithm (like Gradient descent) to find a local optimum. It incorporates not only the first derivative but also the second derivative in its calculations.

In the multidimensional case, this is given by the Hessian matrix.

<p float="left">
   <img src="./res/hess.png">
</p>

