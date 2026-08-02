

let num = [5, 2, 4, 6, 1, 3]


function Insertion_sort(num) {
    for (let i = 1; i < num.length; i++){
        let temp = num[i]
        let j = i - 1
        while (j >= 0 && num[j] > temp) {
            num[j + 1] = num[j]
            j -= 1
        }
        num[j + 1] = temp
    }
}

console.log(Insertion_sort(num))