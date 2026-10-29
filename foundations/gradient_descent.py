class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        if iterations == 0:
            return round(init, 5)

        gradient = 2 * init
        next_x = init - learning_rate * gradient
        
        return self.get_minimizer(iterations -1, learning_rate, next_x)
