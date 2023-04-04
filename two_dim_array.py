import random

def create_array(rows, cols):
    arr = [[random.randint(1, 100) for j in range(cols)] for i in range(rows)]
    return arr

def display_array(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()

def none_element(arr, row, col):
    arr[row][col] = "x"

def blank_element(arr, row, col):
    arr[row][col] = " "

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
arr = create_array(rows, cols)

print("The array is:")
display_array(arr)

# Accessing elements in the array
print("Element in the second row and third column:", arr[1][2])


row_to_delete = int(input("Enter the row index of the element to delete: "))
col_to_delete = int(input("Enter the column index of the element to delete: "))
none_element(arr, row_to_delete, col_to_delete)
print("The array after deleting the element is:")
display_array(arr)

row_to_blank = int(input("Enter the row index of the element to blank out: "))
col_to_blank = int(input("Enter the column index of the element to blank out: "))
blank_element(arr, row_to_blank, col_to_blank)

print("The array after blanking out the element is:")
display_array(arr)

