function bubble(arr){
    for(let i =0; i< arr.length - 1;i++){
        // watch for the length
        for(let j = 0; j < arr.length - 1 - i;j++){
            if (arr[j] > arr[j +1]){
                let temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp 
            }
        }
    }
}
arr = [2,2,2,1]
bubble(arr)
console.log(arr)