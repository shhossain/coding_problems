#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        vector<int> r(8, 0);
        for (int i = 0; i < 8; i++)
        {
            for (int j = 0; j < 8; j++)
            {
                char c;
                cin >> c;
                if (c == 'R')
                {
                    r[i]++;
                }
            }
        }

        // sum r
        int sumr = 0;
        for (int i = 0; i < 8; i++)
        {
            if (r[i] == 1)
            {
                sumr += 1;
            }
        }

        for (int i = 0; i < 8; i++)
        {
            if (r[i] == 8)
            {
                sumr = 8;
            }
        }

        if (sumr == 8)
        {
            cout << "R" << endl;
        }
        else
        {
            cout << "B" << endl;
        }
    }
    return 0;
}