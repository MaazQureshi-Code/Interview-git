function rotate_array(a, b) {
    let n = a.length
    b = b % n
    let res = []
    for (let i = 0; i < a.length; i++){
        res.push(a[(i + b) % n])
    }
    return res
}
console.log(rotate_array([1,2,3],1))