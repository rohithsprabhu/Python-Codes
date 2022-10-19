def fibonacci(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]

# Driver Program for testing
for i in range(1, 11):
    print(fibonacci(i), end=" ")