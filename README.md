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

#### Armijo rule

f($x^k$ - $\tau^k$ grad f($x^k$) - f($x^k$) $\leq$ $\delta$ $\tau$ grad $(f($x^k$))^T$ (- grad f($x^k$)

with $\delta \in (0, 1)$ 

##### Example:

```js
beta = 0.9
while f(x0 - tau * f_grad(x0)) - f(x0) > -eps * f_grad(x0) ** 2
  tau = beta * tau
```


