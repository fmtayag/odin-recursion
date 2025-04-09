function fibs(n) {
    if (n < 0) {
        throw new Error("Negative numbers not allowed.")
    }
    if (n == 0) {
        return [0]
    } 
    
    nums = [0, 1]
    while(nums.length < n + 1) {
        nums.push(
            nums[nums.length-1] + nums[nums.length-2]
        )
    }

    return nums
}

function fibsRec(n) {
    if (n < 0) {
        throw new Error("Negative numbers not allowed.")
    }

    if (n == 0) {
        return [0]
    }

    if (n == 1) {
        return [0, 1]
    }

    if (n < 3) {
        return [0, 1, 1]
    }

    let nums = fibsRec(n-1)
    nums.push(nums[nums.length-1] + nums[nums.length-2])

    return nums
}

console.log(fibsRec(-1))