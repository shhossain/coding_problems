#include <iostream>

using namespace std;

int main()
{

    int i, j, n, t, a, b, sum, sum1, ans;
    cin >> t;
    for (i = 1; i <= t; i++)
    {
        cin >> n >> a >> b;
        ans = a;
        sum = a;
        for (j = 2; j < n; j++)
        {
            cin >> a >> b;
            sum -= b;
            sum += a;
            if (sum > ans)
                ans = sum;
        }
        cout << "Case " << i << ": " << ans << endl;
    }
    return 0;
}