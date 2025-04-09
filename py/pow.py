def myPow(n, p):
    if p == 1:
        return n

    return n * myPow(n, p-1)

print(myPow(2, 16))
