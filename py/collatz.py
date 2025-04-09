def collatz(n, counter=0):
    counter += 1    
    print(round(n))
    
    if n == 1:
        print(f"Number of steps: {counter - 1}")
        return 1

    if n % 2 == 0:
        return collatz(n/2, counter)
    else:
        return collatz((3 * n) + 1, counter)

collatz(15)
