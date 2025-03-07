#Problem50.py
#Project Euler problem 50
import NumberTests
from NumberTests import isPrime
from NumberTests import getFactors


def main():
    sum = 0 
    x = 0
    while x < 1000000:
       if isPrime(x) and isPrime(x) != 1:
          sum = sum + x 
          x = x + 1
    print(sum)
            


        

