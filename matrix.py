import random
import numpy as np

# Create matrix
def create_matrix(rows, cols):
    matrix = [[random.randint(1, 100) for j in range(cols)] for i in range(rows)]
    return matrix

def traverse_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()

def find_element(matrix, row_num, col_num):
    if row_num >= len(matrix) or col_num >= len(matrix[0]):
        return None
    return matrix[row_num][col_num]

def find_element_row_col(matrix, row_num, col_num):
    if row_num >= len(matrix) or col_num >= len(matrix[0]):
        return None
    return matrix[row_num][col_num]

def delete_element(matrix, row_num, col_num):
    if row_num >= len(matrix) or col_num >= len(matrix[0]):
        return None
    deleted_element = matrix[row_num][col_num]
    matrix[row_num][col_num] = 0
    return deleted_element

def print_matrix(matrix):
    print(matrix)

def main():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = create_matrix(rows, cols)

    while True:
        print("\n1. Traverse Matrix")
        print("2. Find Element")
        print("3. Delete Element")
        print("4. Print Matrix")
        print("5. Exit")
        print("6. Find element by row and column index")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            traverse_matrix(matrix)
        elif choice == 2:
            row_num = int(input("Enter row number: "))
            col_num = int(input("Enter column number: "))
            element = find_element(matrix, row_num, col_num)
            if element is None:
                print("Invalid row or column number")
            else:
                print(f"The element at row {row_num} and column {col_num} is {element}")
        elif choice == 3:
            row_num = int(input("Enter row number: "))
            col_num = int(input("Enter column number: "))
            deleted_element = delete_element(matrix, row_num, col_num)
            if deleted_element is None:
                print("Invalid row or column number")
            else:
                print(f"The deleted element is {deleted_element}")
        elif choice == 4:
            print_matrix(matrix)
        elif choice == 5:
            break
        elif choice == 6:
            row_num = int(input("Enter row number: "))
            col_num = int(input("Enter column number: "))
            element = find_element_row_col(matrix, row_num, col_num)
            if element is None:
                print("Invalid row or column number")
            else:
                print(f"The element at row {row_num} and column {col_num} is {element}")
        else:
            print("Invalid choice, please enter a valid choice")

if __name__ == '__main__':
    main()
