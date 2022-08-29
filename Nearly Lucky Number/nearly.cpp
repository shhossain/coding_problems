#include <iostream>
#include <cstring>
using namespace std;
int main()
{
    int i, l, ans = 0;
    string s;
    cin >> s;
    l = s.length();
    for (i = 0; i < l; i++)
    {
        if (s[i] == '7' || s[i] == '4')
            ans++;
    }

    if (ans == 4 || ans == 7)
        cout << "YES\n";
    else
        cout << "NO\n";
    return 0;
}


