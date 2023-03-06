#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    int total = 0;
    int c3 = 0;
    int c2 = 0;
    int c1 = 0;

    for (int i = 0; i < n; i++)
    {
        if (arr[i] == 4)
        {
            total += 1;
        }
        else if (arr[i] == 3)
        {
            c3 += 1;
        }
        else if (arr[i] == 2)
        {
            c2 += 1;
        }
        else if (arr[i] == 1)
        {
            c1 += 1;
        }
    }

    while (c3 > 0 && c1 > 0)
    {
        c3 -= 1;
        c1 -= 1;
        total += 1;
    }

    if (c3 > 0)
    {
        total += c3;
    }

    int v = c2 / 2;
    total += v;
    c2 -= v * 2;

    while (c2 > 0 && c1 > 1)
    {
        c2 -= 1;
        c1 -= 2;
        total += 1;
    }

    while (c2 > 0 && c1 > 0)
    {
        c2 -= 1;
        c1 -= 1;
        total += 1;
    }

    if (c2 > 0)
    {
        total += c2;
    }

    if (c1 > 0)
    {
        v = c1 / 4;
        total += v;
        c1 -= v * 4;

        if (c1 > 0)
        {
            total += 1;
        }
    }

    cout << total << endl;

    return 0;
}