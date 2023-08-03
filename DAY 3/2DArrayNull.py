def zero_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    zero_rows = set()
    zero_cols = set()

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    for i in range(rows):
        for j in range(cols):
            if i in zero_rows or j in zero_cols:
                matrix[i][j] = 0

    return matrix

rows = int(input())
cols = int(input())

matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

result_matrix = zero_matrix(matrix)

for row in result_matrix:
    print(*row)
