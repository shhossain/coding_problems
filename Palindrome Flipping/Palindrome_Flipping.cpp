#include <iostream>
using namespace std;

int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		int n;
		cin >> n;
		int one = 0, zero = 0;
		string s;
		cin >> s;
		for (int i = 0; i < n; i++)
		{
			if (s[i] == '1')
				one++;
			else
				zero++;
		}

		if (one % 2 == 0 || zero % 2 == 0)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}

	return 0;
}