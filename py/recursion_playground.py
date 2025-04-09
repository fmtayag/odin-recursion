def sumRange(n):
    if n == 1:
        return 1

    return n + sumRange(n-1)

def power(n, exp):
    if exp == 1:
        return n

    return n * power(n, exp-1)

def factorial(n):
    if n == 1:
        return n

    return n * factorial(n-1)

def isLessThanSeven(n):
    return n < 7

def myAll(arr, func):
    if len(arr) == 1:
        return func(arr[0])
    
    return myAll(arr[1:], func)

def product(arr):
    if len(arr) == 1:
        return arr[0]

    return arr[0] * product(arr[1:])

def replicate(times, n):
    if times == 1:
        return [n]
    elif times < 0:
        return []

    return [n] + replicate(times-1, n)

def totalIntegers(arr):
    if isinstance(arr, int):
        return 1
    if isinstance(arr, str):
        return 0
    
    total = 0
    for i in range(len(arr)):
        total += totalIntegers(arr[i])

    return total

def sumSquares(arr):
    if isinstance(arr, int):
        return arr * arr

    total = 0
    for i in range(len(arr)):
        total += sumSquares(arr[i])

    return total

##print(sumRange(16))
##print(power(2, 4))
##print(power(2, 16))
##print(factorial(5))
##print(myAll([1,2,9], isLessThanSeven))
##print(product([1,2,3]))
##print(product([1,2,3,10]))
##print(replicate(-3, 5))
##arr = [[[5], 3], 0, 2, ['foo'], [], [4, [5, 6]]]
##print(
##    totalIntegers( arr )
##)
l = [[1,2],3];
print(sumSquares(l))
l = [10,[[10],10],[10]]
print(sumSquares(l))
l = [[[[[[[[[1]]]]]]]]] 
print(sumSquares(l))
