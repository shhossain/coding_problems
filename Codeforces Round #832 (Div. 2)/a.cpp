// for _ in range(int(input())):
//     n = int(input())
//     a = list(map(int, input().split()))
//     g1 = 0
//     g2 = 0

//     for i in range(n):
//         if i >= 0:
//             g1 += a[i]
//         else:
//             g2 += a[i]

//     print(abs(g1)-abs(g2))

#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        ll a[n];
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
        }
        ll g1 = 0;
        ll g2 = 0;
        for (int i = 0; i < n; i++)
        {
            if (a[i] >= 0)
            {
                g1 += a[i];
            }
            else
            {
                g2 += a[i];
            }
        }
        cout << abs(g1) - abs(g2) << endl;
    }
}
