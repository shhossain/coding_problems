#include <iostream>
using namespace std;

int main()
{
	string a;
	cin >> a;
	// check if H in a or Q in a or 9 in a
	if (a.find('H') != string::npos || a.find('Q') != string::npos || a.find('9') != string::npos)
	{
		cout << "YES";
	}
	else
	{
		cout << "NO";
	}

	return 0;
}