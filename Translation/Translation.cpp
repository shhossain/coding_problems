#include <iostream>
using namespace std;

int main(){
    string a = "code";
    string b = "edoc";
    // reverse the string
    string rev = "";
    for (int i = a.length() - 1; i >= 0; i--)
    {
        rev += a[i];
    }

    if (b == rev)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;


}