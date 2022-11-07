#include <iostream>
using namespace std;
int main()
{
    int t, n;
    cin >> t;
    while (t--)
    {
        cin >> n;
        int i, a[n], b[n], c = 0, ca = 0, cb = 0;

        for (i = 0; i < n; i++)
        {
            cin >> a[i];
            if (a[i] == 0)
                ca++;
        }

        for (i = 0; i < n; i++)
        {
            cin >> b[i];
            if (b[i] == 0)
                cb++;
        }

        for (i = 0; i < n; i++)
            if (a[i] != b[i])
                c++;

        int x = abs(ca - cb);
        cout << min(c, x + 1) << endl;
    }
    return 0;
}