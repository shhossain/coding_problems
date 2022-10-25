#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int t;
    cin >> t;
    vector<int> a(2*t+1, -1);
    int b[t];
    int i = 0;
    while (t--)
    {
        int n;
        cin >> n;
        a[2*n] = 0;
        a[2*n+1] = 0;
        b[i] = n;
        i++;
    }

    for (int j = 0; j <= i; ++j)
    {
        int v = b[j];
        int s = v / 2;
        if (a[v] != -1){
            cout << s << endl;
        }
        s++;
        cout << s << endl;
        cout << s << endl;
    }

    return 0;
}