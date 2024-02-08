def pascal_triangle(n):
    """Function to generate Pascal's triangle up to depth n"""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        new_row = [0] * (i + 1)
        new_row[0] = 1
        new_row[-1] = 1

        for j in range(1, len(new_row) - 1):
            a = triangle[i - 1][j]
            b = triangle[i - 1][j - 1]
            new_row[j] = a + b

        triangle.append(new_row)

    return triangle
