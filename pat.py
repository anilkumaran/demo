class Pattern:
    def __init__(self):
        pass

    def generate_spiral_matrix(self, input_number):
        '''
            input_number: 5

            output:
            1   2   3   4   5 
            16  17  18  19  6
            15  24  25  20  7
            14  23  22  21  8
            13  12  11  10  9
        '''
        top_row, bottom_row = 0, input_number - 1
        left_col, right_col = 0, input_number - 1
        self.input_number = input_number
        number = 1

        number_matrix = [
            [0] * input_number
            for _ in range(input_number)
            ]

        while number <= (input_number * input_number):
            # top row
            for i in range(left_col, right_col + 1):
                number_matrix[top_row][i] = number
                number += 1
            
            # right col
            for i in range(top_row+1, bottom_row + 1):
                number_matrix[i][right_col] = number
                number += 1

            # bottom row
            for i in range(right_col-1, left_col-1, -1):
                number_matrix[bottom_row][i] = number
                number += 1
            
            # left col
            for i in range(bottom_row-1, top_row, -1):
                number_matrix[i][left_col] = number
                number += 1

            top_row += 1
            left_col += 1
            bottom_row -= 1
            right_col -= 1

        self.print_spiral_matrix(number_matrix)

    def print_spiral_matrix(self, matrix):
        char_max_len = len(str(self.input_number * self.input_number)) + 1
        for row in matrix:
            for number in row:
                print(str(number).ljust(char_max_len), end=' ')
            print()

input_number = 15
patt_obj = Pattern()
patt_obj.generate_spiral_matrix(input_number)
