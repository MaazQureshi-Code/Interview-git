function mergeSort(arr) {
    if (arr.length <= 1) {
        return arr;
    }
    const divide = Math.floor(arr.length / 2);
    const left = mergeSort(arr.slice(0, divide));
    const right = mergeSort(arr.slice(divide));
    return merge(left, right);
}

function merge(left, right) {
    const result = [];
    let i = 0;
    let j = 0;

    while (i < left.length && j < right.length) {
        if (left[i] <= right[j]) {
            result.push(left[i]);
            i++;
        } else {
            result.push(right[j]);
            j++;
        }
    }
    while (i < left.length) {
        result.push(left[i]);
        i++;
    }
    while (j < right.length) {
        result.push(right[j]);
        j++;
    }

    return result;
}

console.log(mergeSort([8, 3, 5, 1]));
// [1, 3, 5, 8]