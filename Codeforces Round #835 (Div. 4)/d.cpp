#include <iostream>
using namespace std;

#define i1(a) cin >> a;
#define iarr(arr, n)            \
    for (int i = 0; i < n; i++) \
    {                           \
        int x;                  \
        i1(x);                  \
        arr[i] = x;             \
    }

#define print(a) cout << a << endl;
#define loop(n) for (int i = 0; i < n; i++)
#define YES cout << "YES" << endl;
#define NO cout << "NO" << endl;

int main()
{
    int t;
    i1(t);
    loop(t)
    {
        int nn;
        i1(nn);
        int arr[nn];
        iarr(arr, nn);
        int ans = 1;
        bool flag = false;
        for (int i = 0; i < nn - 1 and ans == 1; i++)
        {
            if (arr[i] < arr[i + 1])
            {
                ans = 0;
                while (arr[i + 1] >= arr[i] and i < nn - 1)
                {
                    i++;
                }
                if (i == nn - 1)
                {
                    flag = true;
                    break;
                }
            }
        }

        if (flag || ans == 1)
        {
            YES
        }
        else
        {
            NO
        }
    }

    return 0;
}