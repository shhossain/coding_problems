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
		int a[n]{-1};
		int odd[n]{-1};
		for (int i = 1; i <= n; i++)
		{
			if (i % 2 == 0)
			{
				a[i] = i;
			}
			else
			{
				odd[n - i] = i;
			}
		}

		// print array
		for (int i = 0; i < n; i++)
		{
			if (a[i] != -1)
			{
				cout << a[i] << " ";
			}
		}
		for (int i = 0; i < n; i++)
		{
			if (odd[i] != -1)
			{
				cout << odd[i] << " ";
			}
		}
		cout << endl;
	}

	return 0;
}