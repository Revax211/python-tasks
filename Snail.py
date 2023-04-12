# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python
# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:
# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]

def snail(array):
    if not array or not any(array):
        return []
    result = []
    n = len(array)
    visited = [[False] * n for _ in range(n)]
    top = 0
    bottom = n - 1
    left = 0
    right = n - 1
    while left <= right and top <= bottom:
        for i in range(left, right+1):
            if not visited[top][i]:
                result.append(array[top][i])
                visited[top][i] = True
        top += 1
        for i in range(top, bottom+1):
            if not visited[i][right]:
                result.append(array[i][right])
                visited[i][right] = True
        right -= 1
        for i in range(right, left-1, -1):
            if not visited[bottom][i]:
                result.append(array[bottom][i])
                visited[bottom][i] = True
        bottom -= 1
        for i in range(bottom, top-1, -1):
            if not visited[i][left]:
                result.append(array[i][left])
                visited[i][left] = True
        left += 1
    return result