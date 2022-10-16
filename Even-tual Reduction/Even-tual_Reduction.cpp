#include <iostream>
#include <map>
using namespace std;

int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		int n;
		string s;
		cin >> n >> s;
		map<char, int> m;
		for (int i = 0; i < n; i++)
		{
			m[s[i]]++;
		}
		bool flag = false;
		// loop through the map
		for (pair<char, int> p : m)
		{
			if (p.second % 2 != 0)
			{
				flag = true;
				break;
			}
		}
		if (flag)
		{
			cout << "NO" << endl;
		}
		else
		{
			cout << "YES" << endl;
		}
	}

	return 0;
}