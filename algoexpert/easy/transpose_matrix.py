# with pre initialization
def transpose_with_init(matrix):
    row_cnt = len(matrix)
    col_cnt = len(matrix[0])
    ans = [[0 for _ in range(row_cnt)] for _ in range(col_cnt)]
    for col_ind in range(col_cnt):
        for row_ind in range(row_cnt):
            ans[col_ind][row_ind] = matrix[row_ind][col_ind]
    return ans


# with append
def transpose_with_append(matrix):
    row_cnt = len(matrix)
    col_cnt = len(matrix[0])
    ans = []
    for col_ind in range(col_cnt):
        new_row = []
        for row_ind in range(row_cnt):
            new_row.append(matrix[row_ind][col_ind])
        ans.append(new_row)
    return ans


def main():
    matrix = [[1, 2, 3], [4, 5, 6]]
    print(transpose_with_init(matrix))
    print(transpose_with_append(matrix))


if __name__ == "__main__":
    main()
