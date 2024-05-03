class fib():
    def fibonacci(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        
        return b
    
# test = fib()
# print("the", str(10)+"th fibonacci number is", str(test.fibonacci(10)))
