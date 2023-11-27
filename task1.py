matrix = [
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
    ]
def symmetrical(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return True
    return False

if symmetrical(matrix):
    print("Граф орієнтований.")
else:
    print("Граф може бути як неорієнтованим, так і орієнтованим.")



