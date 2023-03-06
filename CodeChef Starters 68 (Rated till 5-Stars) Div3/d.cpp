#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main()
{
    ll t;
    cin >> t;
    while (t--)
    {
        ll n, ans = 0;
        ;
        cin >> n;
        string s;
        cin >> s;
        map<pair<char, ll>, ll> mp;
        char current = s[0];
        ll length = 1;
        mp[{current, length}]++;
        for (ll i = 1; i < n; i++)
        {
            if (current != s[i])
            {
                length = 1;
                current = s[i];
            }
            else
                length++;

            mp[{current, length}]++;
        }
        for (auto x : mp)
        {
            if (x.second == 1)
            {
                ans = max(ans, x.first.second - 1);
            }
            else
                ans = max(ans, x.first.second);
        }

        cout << ans << endl;
    }
}