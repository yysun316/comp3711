#include <iostream>
using namespace std;

int fibonacci_recursion(int n){
    if (n <= 1)
        return n;
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2);
}

int fib_bottom_up(int n)
{
    int f[n + 2]; // 1 extra to handle case, n = 0
    int i;
    f[0] = 0;
    f[1] = 1;
    for (i = 2; i <= 0; i++)
        f[i] = f[i - 1] + f[i - 2];
    return f[n];
}

int main(void) {
    int n = 9;
    cout << fibonacci_recursion(n) << endl;
    return 0;
}