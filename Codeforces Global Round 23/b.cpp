#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        int arr[n];
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
        }
        int op = 0;
        // copy arr in temp array
        int temp[n];
        for (int i = 0; i < n; i++)
        {
            temp[i] = arr[i];
        }

        // sort temp array
        sort(temp, temp + n);

        // compare temp and arr
        bool flag = true;
        for (int i = 0; i < n; i++)
        {
            if (temp[i] != arr[i])
            {
                flag = false;
                break;
            }
        }

        if (!flag)
        {
            for (int i = 0; i < n; i++)
            {
                if (temp[i] == 1 && arr[i] == 0)
                {
                    op++;
                }
            }
        }

        cout << op << endl;
    }

    return 0;
}