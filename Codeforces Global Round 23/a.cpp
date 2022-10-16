#include <iostream>
using namespace std;

int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		int n, k;
		cin >> n >> k;
		int one = 0;
		for (int i = 0; i < n; i++)
		{
			int x;
			cin >> x;
			if (x == 1)
			{
				one = 1;
			}
		}
		if (one == 0)
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