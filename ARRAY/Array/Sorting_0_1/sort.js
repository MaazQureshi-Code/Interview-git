
let arr = [0, 1, 1, 0, 1, 0, 0, 1];
arr.sort((a, b) => a - b );
console.log(arr);
function sort01(arr) {
    let left = 0;
    let right = arr.length - 1

    while(left < right){

	while(left < right && arr[left] == 0){left++}
	while(left < right && arr[right] == 1){right--}
	
	if(left < right){
		arr[left] = 0;
		arr[right] = 1;
		left++
		right--
	}


}

}