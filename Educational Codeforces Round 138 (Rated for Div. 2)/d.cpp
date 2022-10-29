#include <iostream>
using namespace std;

int abs_val(int val)
{
    if (val < 0)
    {
        return -val;
    }
    return val;
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, q;
        cin >> n >> q;
        int a[n];
        int a_sum = 0;
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
            a_sum += a[i];
        }

        for (int i = 0; i < q; i++)
        {
            int a, b;
            cin >> a >> b;
            int v = abs_val(a - b) + 1;
            if (v % 2 != 0)
            {
                a_sum += 1;
            }
        }

        cout << a_sum << endl;
    }
}