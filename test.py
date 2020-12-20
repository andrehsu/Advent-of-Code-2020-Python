import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def print_arr(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i, j], end=' ')
        print()
    print()


print_arr(arr)

arr = np.rot90(arr)
print_arr(arr)

arr = np.flipud(arr)
print_arr(arr)
