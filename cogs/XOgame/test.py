import numpy as np

A = np.array([[0,2,2],
              [1,2,1],
              [0,2,0]])



def row_completed(grid):

    print("searching for completion in rows")
    result_list = []

    for row in grid:
        if 0 not in row:
            if row[0] == row[1]:
                if row[1] == row[2]:
                    result_list.append(True)
                else:
                    result_list.append(False)
            else:
                result_list.append(False)
        else:
            result_list.append(False)

    if True in result_list:
        print('found completion in rows')
        return True
    else:
        print("row not completed")
        return False


def column_completed(grid):

        result_list = []

        print("searching for completion in columns")

        for row in grid.transpose():
            if 0 not in row:
                if row[0] == row[1]:
                    if row[1] == row[2]:
                        result_list.append(True)
                    else:
                        result_list.append(False)
                else:
                    result_list.append(False)
            else:
                result_list.append(False)

        if True in result_list:
            print("completion found in columns")
            return True

        else:
            print("failed to find completion in columns")
            return False

def diagonal_completed(grid):

        print("searching for completion in diagonals")

        diag1 = np.diagonal(grid)
        diag2 = np.diagonal(np.rot90(grid))

        result_list = []
        if 0 not in diag1:
            if diag1[0] == diag1[1]:
                if diag1[1] == diag1[2]:
                    result_list.append(True)
                else:
                    result_list.append(False)
            else:
                result_list.append(False)
        elif 0 not in diag2:
            if diag2[0] == diag2[1]:
                if diag2[1] == diag2[2]:
                    result_list.append(True)
                else:
                    result_list.append(False)
            else:
                result_list.append(False)
        else:
            result_list.append(False)


        if True in result_list:
            print("completion found in diagonals")
            return True

        else:
            print("failed to find completion in diagonals")
            return False

def is_won(A):
        grid = A

        if row_completed(grid):
            return True
        elif column_completed(grid):
            return True
        elif diagonal_completed(grid):
            return True
        else:
            return False

print(is_won(A))