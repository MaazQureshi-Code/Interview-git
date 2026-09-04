

function findOccurence(num) {
    let count = {}

    for (let i of num) {
        if (count[i] !== undefined) {
            count[i] += 1
        } else {
            count[i] = 1
        }
    }


    return Object.values(count)
}




console.log(findOccurence([1,2,3,4]))