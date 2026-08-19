function quickSort(arr, low, high) {
    if (low < high) {
        let pivot_index = partition(arr, low, high)
        quickSort(arr, low, pivot_index - 1)
        quickSort(arr, pivot_index + 1, high)
    }
}

function partition(arr, low, high) {
    let pivot = arr[low]
    let i = low
    for (let j = low + 1; j < high + 1; j++) {
        if (arr[j] < pivot) {
            i = i + 1
            let temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        }
    }
    let temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp
    return i
}

let numbers = [7, 2, 9, 4, 1]
quickSort(numbers, 0, 4)
console.log(numbers)   //   Quick sort does not return a array it just change the array 