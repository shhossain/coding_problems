#include <iostream>
using namespace std;

int main()
{
	int a, b, count = 0;
	cin >> a >> b;

	while (1)
	{
		if (a > b)
		{
			break;
		}
		a *= 3;
		b *= 2;
		count++;
	}
	cout << count;

	return 0;
}