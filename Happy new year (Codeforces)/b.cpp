#include <iostream>
using namespace std;
int main()
{

    int t;
    cin >> t;
    while (t--)
    {

        int a, b, x, y;
        cin >> a >> b;
        x = min(a, b);
        y = (a + b) / 4;
        cout << min(x, y) << endl;
    }
    return 0;
}