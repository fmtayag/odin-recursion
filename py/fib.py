def fibs(n):
    if n == 0:
        return [0]

    nums = [0, 1]

    while(len(nums) < n + 1):
        nums.append(nums[-1] + nums[-2])

    return nums

def fibsRec(n):
    if n == 0:
        return [0]
    if n < 2:
        return [0, 1]
    if n < 3:
        return [0, 1, 1]

    nums = fibsRec(n-1)
    nums.append(nums[-1] + nums[-2])

    return nums

x = 4
print(f"Hey: {fibs(x)}")
print(f"Hey: {fibsRec(x)}")
