#include <iostream>
#include <string>
using namespace std;

bool nearly_lucky(string s)
{
    int len = s.length();
    // len is 4 or 7 or return false
    if (len != 4 && len != 7)
        return false;

    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == '4' || s[i] == '7')
        {
            continue;
        }
        else
        {
            return false;
        }
    }
    return true;
}

int main()
{
    string a = "7747774";

    if (nearly_lucky(a))
        cout << "YES" << endl;
    else
        cout << "NO" << endl;

    return 0;
}
