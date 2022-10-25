// t = int(input())
// for i in range(t):
//     n = int(input())
//     a1 = list(map(int, input().split()))
//     a2 = list(map(int, input().split()))
//     a = [[i, j] for i, j in zip(a1, a2)]
//     b = sorted(a, key=lambda x: x[1])
//     t = 0
//     for i in range(len(b)):
//         if i < len(b)-1:
//             b[i+1][0] += b[i][1]
//         t += b[i][0]
//     print(t)
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        vector<long long> a1(n);
        vector<long long> a2(n);
        for (int i = 0; i < n; i++)
        {
            cin >> a1[i];
        }
        for (int i = 0; i < n; i++)
        {
            cin >> a2[i];
        }
        vector<vector<long long>> a(n, vector<long long>(2));
        for (int i = 0; i < n; i++)
        {
            a[i][0] = a1[i];
            a[i][1] = a2[i];
        }
        sort(a.begin(), a.end(), [](vector<long long> a, vector<long long> b)
             { return a[1] < b[1]; });
        long long total = 0;
        for (int i = 0; i < n; i++)
        {
            if (i < n - 1)
            {
                a[i + 1][0] += a[i][1];
            }
            total += a[i][0];
        }
        cout << total << endl;
    }
}
