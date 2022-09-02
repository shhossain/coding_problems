#include <bits/stdc++.h>

using namespace std;

int main()
{

    int a, b, c, n1, n2, n3, n4, max;
    cin >> a >> b >> c;
    n1 = a + b * c;
    n2 = a * (b + c);
    n3 = a * b * c;
    n4 = (a + b) * c;
    max = (n1 > n2 && n1 > n3 && n1 > n4) ? n1 : ((n2 > n3 && n2 > n4) ? n2 : (n3 > n4 ? n3 : n4));
    cout << max << endl;

    return 0;
}