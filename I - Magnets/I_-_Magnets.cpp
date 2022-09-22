#include <iostream>
using namespace std;

int main()
{
	int n;
	cin >> n;
	int plus_minus = 0, minus_plus = 0;
	bool plus = false;
	bool minus = false;
	for (int i = 0; i < n; i++)
	{
		int num;
		cin >> num;

		if (num == 10 && plus == false)
		{
			plus_minus++;
			plus = true;
			minus = false;
		}
		else if (num == 1 && minus == false)
		{
			minus_plus++;
			minus = true;
			plus = false;
		}
	}
	cout << plus_minus + minus_plus;
	return 0;
}