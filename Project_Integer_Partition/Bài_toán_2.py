def count_partitions(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for j in range(k + 1):
        dp[0][j] = 1

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if i >= j:
                dp[i][j] = dp[i - j][j] + dp[i][j - 1]
            else:
                dp[i][j] = dp[i][j - 1]
    return dp[n][k]

n, k = 5, 3
print(f"p({n}, {k}) =", count_partitions(n, k))
