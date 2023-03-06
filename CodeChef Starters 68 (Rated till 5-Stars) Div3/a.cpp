#include <iostream>
#include <cstdlib>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int a, c;
        cin >> a >> c;
        int v = -1;
        for (int i = a; i <= c; i++)
        {
            if (abs(a - i) == abs(c - i))
            {
                v = i;
            }
        }
        cout << v << endl;
    }
}