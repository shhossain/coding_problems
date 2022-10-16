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

        int left = 0;
        int right = n - 1;
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
            while (left < right)
            {
                while (arr[left] == 0)
                {
                    left++;
                }
                while (arr[right] == 1)
                {
                    right--;
                }
                if (left < right)
                {
                    arr[left] = 0;
                    arr[right] = 1;
                    left++;
                    right--;
                }

                op++;
            }
        }

        cout << op << endl;
    }

    return 0;
}