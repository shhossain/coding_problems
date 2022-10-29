
#include <iostream>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        string s;
        cin >> s;
        int c = 0;
        int total = 0;
        bool cluster = false;
        for (int i = 0; i < n; i++)
        {
            if (s[i] == '1')
            {
                c = i + 1;
            }
            if (s[i] == '1' && !cluster)
            {
                total++;
                cluster = true;
            }
            else if (s[i] == '0')
            {
                cluster = false;
            }
        }

        if (c == n)
        {
            total--;
        }
        cout << total << endl;
    }
}