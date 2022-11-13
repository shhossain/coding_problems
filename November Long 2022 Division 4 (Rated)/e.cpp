#include <iostream>
using namespace std;
#define ll long long
#define mod 1000000007
#define MAX 1000001
ll facts[MAX + 1];

void precompute()
{
    facts[0] = 1;
    facts[1] = 1;
    ll s = 1;
    for (int i = 2; i <= MAX; i++)
    {
        s = ((s % mod) * (i % mod)) % mod;
        facts[i] = s;
    }
}

int main()
{
    precompute();
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        ll asum = 0;
        for (int i = 0; i < n; i++)
        {
            int x;
            cin >> x;
            asum += facts[x];
        }
        cout << asum % mod << endl;
    }
    return 0;
}