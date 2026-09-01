



function Spiral(num) {
    top = 0  //we check the 
    bottom = num.length - 1
    left = 0 
    right = num[0].length - 1
    while (top <= bottom && left <= right) {
        
        // Here we trace the First row
        
        col = left
        while (col <= right) {
            console.log(num[top][col] + "\t")
            col += 1
        }
        // Here we trace the down here
        row = top + 1
        while (row <= bottom) {
            console.log(num[row][right])
            row += 1
        }

        // we go with the left side and a condition
        col = right - 1
        if (top < bottom) {
            
            while (col >= left) {
                console.log(num[bottom][col])
                col -= 1
            }
        }
        if (left < right) {
            row = bottom - 1
            while (row > top) {
                console.log(num[row][left])
                row -= 1
            }
        }

        top += 1
        bottom -= 1
        left += 1
        right -= 1
    
    }
}





console.log(
    Spiral(
    [[1, 2, 3]
    ,[4, 5, 6],
     [7, 8, 9]]))