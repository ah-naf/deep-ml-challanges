def mean(values):
    return sum(values) / len(values)

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    n, k = len(vectors), len(vectors[0])
    means = [mean(vectors[i]) for i in range(n)]
    
    cov = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            total = 0
            for t in range(k):
                total += (vectors[i][t] - means[i]) * (vectors[j][t] - means[j])
            cov[i][j] = total / (k-1)
    return cov

x = [[1, 2, 3], [4, 5, 6]]
print(calculate_covariance_matrix(x))