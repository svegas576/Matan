import sympy
import math
def y(n):
    f = n**n/math.factorial(n)     #выдает ошибку factorial() only accepts integral values
    y = sympy.limit(f,n,math.inf)
    print(y.Decimal(0.0000001))
y(math.inf)
