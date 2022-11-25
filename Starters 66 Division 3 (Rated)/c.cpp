#include <iostream>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, m, k, x,val;
        cin >> n >> m >> k >> x;
        val = x % (n * k + m);
        if (val != 0 && (val - (n * (k - 1))) <= 0)
        {
            cout << "NO" << endl;
        }
        else
            cout << "YES" << endl;
    }
    return 0;
}