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
		cin >> n;
		map<int, int> m;
		for (int i = 0; i < n; i++)
		{
			int x;
			cin >> x;
			m[x]++;
		}

		// get max value of map
		int max_value = 0;
		for (auto it = m.begin(); it != m.end(); it++)
		{
			if (it->second > max_value)
			{
				max_value = it->second;
			}
		}
		cout << n - max_value << endl;
	}
	return 0;
}