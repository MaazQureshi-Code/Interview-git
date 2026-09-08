

function NobleInteger(A) {

    // In javascript
    A.sort((a, b) => a - b)
    let n = A.length
    
    for (i = 0; i < A.length; i++){
        
        if (i < n - 1 && A[i] === A[i + 1]) {
            continue
        }

        let greater = n - i - 1

        if (A[i] == greater) {
            return 1
        }
    }
    return -1
}
let x = NobleInteger([1, 2, 2])

console.log(x)