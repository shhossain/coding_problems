#include <bits/stdc++.h>
using namespace std;

int main()
{
    int i, n;
    string s, t;
    cin >> s >> t;
    n=s.length();

    for (i = 0; i < n / 2; i++)
        swap(s[i], s[n - i - 1]);

    if (s == t)
        cout << "Yes\n";
    else
        cout << "No\n";
    return 0;
}