function selectionSort(arr) {
    for (let i = 0; i < arr.length - 1; i++) {
        let minIndex = i               // assume current position holds the smallest

        for (let j = i + 1; j < arr.length; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j            // found a smaller one, remember its index
            }
        }

        if (minIndex !== i) {           // only swap if we actually found something smaller
            let temp = arr[i]
            arr[i] = arr[minIndex]
            arr[minIndex] = temp
        }
    }
}

let numbers = [7, 2, 9, 4, 1]
selectionSort(numbers)
console.log(numbers)