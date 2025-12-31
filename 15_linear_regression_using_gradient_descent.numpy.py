import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
      """
	  Perform linear regression using gradient descent.

	  m = number of training examples
	  n = number of parameters (features), technically n-1 features, 1st column is for intercept

	  X: shape (m, n), `m` training examples with `n` input values for each feature
	  y: shape (m, 1) array with the target values (ground truth)
	  alpha: learning rate
      iterations: number of gradient descent steps
      """
      m, n = X.shape
      y = y.reshape(-1, 1) 	# Make sure y is a column vector
      theta = np.zeros((n, 1))

      for _ in range(iterations):
        predictions = np.zeros((m, 1))
        for i in range(m):
            s = 0
            for j in range(n):
                s += X[i][j] * theta[j][0]
            predictions[i][0] = s
        
        gradients = np.zeros((n, 1))
        for j in range(n):
            grad_sum = 0
            for i in range(m):
                grad_sum += (predictions[i][0] - y[i][0]) * X[i][j]
            gradients[j][0] = grad_sum / m
        
        for j in range(n):
            theta[j][0] -= alpha * gradients[j][0]
    
      return np.round(theta.flatten(), 4)


X = np.array([[1, 1], [1, 2], [1, 3]])
y = np.array([1, 2, 3])
alpha = 0.01
iterations = 1000

print(linear_regression_gradient_descent(X, y, alpha, iterations))