#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n;
    cin >> n;
    fflush(stdin);
    string s;
    getline(cin, s);
    reverse(s.begin(), s.end());
    cout << s << endl;
}