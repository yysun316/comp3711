# Adding 2 nums
def sum(x,y,n,z):
    c = 0
    for i in range(n):
        z[i] = x[i] + y[i] + c
        if z[i] >= 10:
            c = 1
            z[i] = z[i] - 10
        else:
            c = 0
    z[n] = c

def test1():
    x = [int(digit) for digit in str(529501233)][::-1]
    y = [int(digit) for digit in str(612345678)][::-1]
    print(x)
    print(y)
    z = [0 for i in range(10)]
    sum(x,y,9,z)
    return z[::-1]

if __name__ == '__main__':
    print(test1())
