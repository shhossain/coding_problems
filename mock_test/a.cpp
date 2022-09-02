#include <iostream>
using namespace std;

int main()
{
    // 10^12
    int runs = 10;
    for (int i = 0; i < runs; i++)
    {
        string s;
        cin >> s;

        // if s == 0 then break
        if (s == "0")
            break;

        long long int_s = stoll(s);
        if (int_s > 10)
        {
            string last_char = s.substr(s.length() - 1);
            // int last char max length is 10^12
            long long last_int = stoll(last_char);

            string remaining_char = s.substr(0, s.length() - 1);
            long long remaining_int = stoll(remaining_char);

            // cout << remaining_int <<" -- "<< last_int << endl;

            long long val = remaining_int - (last_int * 5);

            if (val % 17 == 0)
            {
                cout << 1 << endl;
            }
            else
            {
                cout << 0 << endl;
            }
        }
        else
        {
            cout << 0 << endl;
        }
    }
}