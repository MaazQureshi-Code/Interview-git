def Spiral(num):
    if not num:
        return []

    top = 0
    bottom = len(num) - 1
    left = 0
    right = len(num[0]) - 1

    while top <= bottom and left <= right:

        # 1. Move RIGHT
        col = left
        while col <= right:
            print(num[top][col])
            col += 1

        # 2. Move DOWN
        row = top + 1
        while row <= bottom:
            print(num[row][right])
            row += 1

        # 3. Move LEFT
        # Only if there is another row
        if top < bottom:
            col = right - 1
            while col >= left:
                print(num[bottom][col])
                col -= 1

        # 4. Move UP
        # Only if there is another column
        if left < right:
            row = bottom - 1
            while row > top:
                print(num[row][left])
                row -= 1

        # Shrink the box
        top += 1
        bottom -= 1
        left += 1
        right -= 1


Spiral([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])