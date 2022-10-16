#include <iostream>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, q;
        cin >> n >> q;
        long long a[n];
        long long sum = 0;
        int e = 0;
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
            sum += a[i];
            if (a[i] % 2 == 0)
            {
                e++;
            }
        }
        int o = n - e;
        for (int i = 0; i < q; i++)
        {
            int d, v;
            cin >> d >> v;
            if (d == 0)
            {
                sum += (v * e);
                if (v % 2 != 0)
                {
                    int temp = e;
                    e -= temp;
                    o += temp;
                }
            }
            else
            {
                sum += (v * o);
                if (v % 2 != 0)
                {
                    int temp = o;
                    o -= temp;
                    e += temp;
                }
            }
            cout << sum << endl;
        }
    }
    return 0;
}