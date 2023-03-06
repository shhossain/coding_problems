# #include <bits/stdc++.h>
# using namespace std;
# #define ll long long
# #define fl(n) for (int i = 0; i < n; i++)
# #define flj(n) for (int j = 0; j < n; j++)
# int main()
# {

#     int t;
#     cin >> t;
#     while (t--)
#     {
#         ll x, y, a, b = 0, c = 0, ans, count = 0;
#         cin >> a;
#         for (int i = a; i > 0; i--)
#         {
#             if (i % 3 == 0)
#             {
#                 ans = i / 3;
#                 break;
#             }
#             else
#                 count++;
#         }
#         if (count % 2 == 0)
#             b += count / 2, c += count / 2;
#         else
#             c += count;

#         cout << ans << " " << ans + b << " " << ans + c << endl;
#     }
#     return 0;
# }

for _ in range(int(input())):
    a = int(input())
    ans = 0
    ct = 0
    b = 0
    c = 0
    for i in range(a, 0, -1):
        if i % 3 == 0:
            ans = i//3
            break
        else:
            ct += 1

    if ct % 2 == 0:
        b += ct//2
        c += ct//2
    else:
        c += ct
    print(ans, ans+b, ans+c)
