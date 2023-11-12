#include <iostream>
#include <string.h>
using namespace std;

void printSubStr(string str, int low, int high)
{
    for (int i = low; i <= high; ++i)
        cout << str[i];
}

int longestPalSubstr(string str)
{
    int n = str.size();
    int maxLength = 1, start = 0;

    for (int i = 0; i < str.length(); ++i)
        for (int j = i; j < str.length(); ++j)
        {
            int flag = 1;

            for (int k = 0; k < (j - i + 1) / 2; k++)
                if (str[i + k] != str[j - k])
                {
                    flag = 0;
                    break;
                }
            if (flag && (j - i + 1) > maxLength)
            {
                start = i;
                maxLength = j - i + 1;
            }
        }

    cout << "Longest palindrome substring is: ";
    printSubStr(str, start, start + maxLength - 1);

    return maxLength;
}

/*
DP:


*/
class Solution
{
public:
    string longestPalindrome(string s)
    {
        int n = s.size();
        bool dp[n][n];
        memset(dp, 0, sizeof(dp));
        int start = 0, maxLength = 1; // starting index and maxLength of lPS
        for (int i = 0; i < n; ++i)
        {
            dp[i][i] = true; // diagonal
            if (i + 1 < n && s[i] == s[i + 1])
            {
                dp[i][i + 1] = true;
                start = i;
                maxLength = 2;
            }
        }
        // check for lengths greater than 2, k: len
        for (int k = 3; k <= n; ++k)
        {
            //  i: start index
            for (int i = 0; i < n - k + 1; ++i)
            {
                // j: end index
                int j = i + k - 1;
                // Is palindrome conditions: 1) starting element = ending element
                // 2) inner element (dp) are equal
                if (s[i] == s[j] && dp[i + 1][j - 1])
                {
                    dp[i][j] = true;
                    if (k > maxLength)
                    { // ensure that maxLength only update once
                        maxLength = k;
                        start = i;
                    }
                }
                else
                    dp[i][j] = false;
            }
        }
        return s.substr(start, maxLength);
    }
};

int main()
{
    string str = "forgeeksskeegfor";
    cout << "\nLength is: " << longestPalSubstr(str);
    return 0;
}