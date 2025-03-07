#Problem10.py
#Project Euler problem 10
import NumberTests
from NumberTests import isPrime


def main():
    primeNums = 0 
    for i in range(2000000):
        if isPrime(i) and i != 1:
           primeNums += i
           
    print(primeNums)
    #tested with smaller numbers, 2million just takes a long time
        

if __name__ == '__main__':
  main()