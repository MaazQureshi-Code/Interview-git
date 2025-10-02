

function merge(arr1, arr2) {

    const totalLength = arr1.length + arr2.length;
    const mergedArray = new Array(totalLength);
    let index = 0;
    let i = 0, j = 0;

    while (i < arr1.length && j < arr2.length) {
        if(arr1[i] < arr2[j]){
            mergedArray[index++] = arr1[i++];
        }else{
            mergedArray[index++] = arr2[j++];
        }
        
    }

    while (i < arr1.length) {
        mergedArray[index++] = arr1[i++];
    }
    while (j < arr2.length) {
        mergedArray[index++] = arr2[j++];
    }


    return mergedArray;
    }

    function heapMerge(arr1, arr2) {
        /// Second ways of the merge
      let mergedArray = [...arr1, ...arr2];
      mergedArray.sort((a, b) => a - b);
        return mergedArray;
    }