def matrix_chain_order(p):
    # m[i][j]存储从第i个矩阵到第j个矩阵的最小计算代价
    # s[i][j]存储最优的分割点
    n = len(p) - 1
    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]

    for chain_length in range(2, n + 1):
        for i in range(1, n - chain_length + 2):
            j = i + chain_length - 1
            # 将矩阵m[i][j]初始值设为无穷大
            # 以确保在算法的执行过程中可以找到更小的值
            m[i][j] = float("inf")
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s


def print_Parenthes(s, i, j):
    # 如果 i 和 j 相等，表示链中只有一个矩阵，直接打印矩阵的标识符。

    if i == j:
        print(f"A{i}", end="")
        # 带有 f-string（格式化字符串字面值）的字符串
    else:
        print("(", end="")
        print_Parenthes(s, i, s[i][j])
        print_Parenthes(s, s[i][j] + 1, j)
        print(")", end="")


matrix_dimensions = [30, 35, 15, 5, 10, 20, 25]
m, s = matrix_chain_order(matrix_dimensions)
print("Min cost:", m[1][len(matrix_dimensions) - 1])
print_Parenthes(s, 1, len(matrix_dimensions) - 1)
