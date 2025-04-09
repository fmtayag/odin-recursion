function mergeSort(nums) {
    if (nums.length == 1) {
        return nums
    }
    
    let left = mergeSort(getLeft(nums))
    let right = mergeSort(getRight(nums))

    let merged = []
    let leftPtr = 0
    let rightPtr = 0
    while(true) {
        /* End branches */
        if(right.length == rightPtr) {
            merged.push(...left.slice(leftPtr, left.length))
            break
        }
        if(left.length == leftPtr) {
            merged.push(...right.slice(rightPtr, right.length))
            break
        }

        /* Merge branches */
        /* Note: Flip the comparison operator to descend. 
            > Ascending
            < Descending
        */
        if(left[leftPtr] > right[rightPtr]) {
            merged.push(right[rightPtr])
            rightPtr++
        }
        else {
            merged.push(left[leftPtr])
            leftPtr++
        }
    }

    // console.log(`Merged: ${merged} | \t\t\tLeft: ${left} | Right: ${right}`)
    
    return merged
}

const getDivisor = (arr) => Math.floor(arr.length / 2)
const getLeft = (arr) => arr.slice(0, getDivisor(arr))
const getRight = (arr) => arr.slice(getDivisor(arr), arr.length)

let x = 100;
// let arr = Array.from({length: x}, () => Math.floor(Math.random() * x))
let arr = [6, 3, 2, 4, 1, 5]
console.log(arr);
console.log(mergeSort(arr))

// /* Divide */
// let left = getLeft(arr)
// let right = getRight(arr)

// let left_left = getLeft(left)
// let left_right = getRight(left)

// let left_right_left = getLeft(left_right)
// let left_right_right = getRight(left_right)

// /* Merge */
// let y = left_right_left.concat(left_right_right)
// let x = Math.min(y)

// console.log(x)
// mergeSort(arr)
