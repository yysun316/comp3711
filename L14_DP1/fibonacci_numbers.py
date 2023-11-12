from ctypes import sizeof


def fibonacci_recursion(n):
    if n <= 1:
        return n
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

#O(n) time, O(n) space
def fibonacci_bottom_up(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]


F = [0 for _ in range(10)] # At most 10 numbers
F[0] = 0
F[1] = 1
def fibonacci_top_down(n):
    if F[n] != 0 or n == 0 or n == 1:
        return F[n]
    F[n] = fibonacci_top_down(n-1) + fibonacci_top_down(n-2)
    return F[n]

print(fibonacci_top_down(9))
print(F[9])