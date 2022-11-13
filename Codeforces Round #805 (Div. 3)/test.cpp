#include <iostream>
#include <set>
using namespace std;
#define ll long long
#define fl(n) for (int i = 0; i < n; i++)
int main()
{

    int t;
    cin >> t;
    while (t--)
    {
        ll c = 0;
        string s;
        cin >> s;
        set<char> ch;

        fl(s.length())
        {
            ch.insert(s[i]);
            // cout << ch.size() << endl;
            if (ch.size() == 3)
            {
                ch.insert(s[i + 1]);
                cout << "i+1" << s[i+1] << " " << endl;
                cout << ch.size() << endl;
            }
        }
   
    }
    return 0;
}