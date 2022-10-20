#include <iostream>
using namespace std;
int main()
{
    int t, n, x;
    cin >> t;
    while (t--)
    {
        cin >> n;
        int arr[n];
        int sum = 0;
        for (int i = 0; i < n; i++)
            cin >> arr[i];
        x = 9 - n;
        for (int i = 1; i <= x; i++)
            sum += 6 * i;
        cout << sum << endl;
    }
}