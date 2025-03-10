def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([0] * m)
        for j in range(m):
            matrix[i][j] = value
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)

# такой вывод нагляднее
# for i in result1:
#     print(i)
# for i in result2:
#     print(i)
# for i in result3:
#     print(i)
