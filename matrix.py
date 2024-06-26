class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = []

    def read_matrix(self):
        print(f"Enter {self.rows} rows and {self.cols} columns for the matrix:")
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                element = float(input(f"Enter element at position ({i+1}, {j+1}): "))
                row.append(element)
            self.matrix.append(row)

    def display_matrix(self):
        for row in self.matrix:
            print(row)

    def add_matrices(self, other_matrix):
        if self.rows != other_matrix.rows or self.cols != other_matrix.cols:
            print("Matrices must have the same dimensions for addition.")
            return None
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.matrix[i][j] + other_matrix.matrix[i][j])
            result.matrix.append(row)
        return result

    def multiply_matrices(self, other_matrix):
        if self.cols != other_matrix.rows:
            print("Number of columns in the first matrix must match the number of rows in the second matrix for multiplication.")
            return None
        result = Matrix(self.rows, other_matrix.cols)
        for i in range(self.rows):
            row = []
            for j in range(other_matrix.cols):
                element = 0
                for k in range(self.cols):
                    element += self.matrix[i][k] * other_matrix.matrix[k][j]
                row.append(element)
            result.matrix.append(row)
        return result

# Menu-driven program
def main():
    rows = int(input("Enter the number of rows for the matrices: "))
    cols = int(input("Enter the number of columns for the matrices: "))
    matrix1 = Matrix(rows, cols)
    matrix2 = Matrix(rows, cols)

    print("\nMatrix 1:")
    matrix1.read_matrix()

    print("\nMatrix 2:")
    matrix2.read_matrix()

    while True:
        print("\nMenu:")
        print("1. Display matrices")
        print("2. Add matrices")
        print("3. Multiply matrices")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("\nMatrix 1:")
            matrix1.display_matrix()
            print("\nMatrix 2:")
            matrix2.display_matrix()
        elif choice == 2:
            result = matrix1.add_matrices(matrix2)
            if result:
                print("\nResult of addition:")
                result.display_matrix()
        elif choice == 3:
            result = matrix1.multiply_matrices(matrix2)
            if result:
                print("\nResult of multiplication:")
                result.display_matrix()
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()