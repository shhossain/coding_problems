#include <iostream>
#include <vector>
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
		int count = 0;
		bool flag = false;
		for (int i = 0; i < n; i++)
		{
			// count the number of consonants
			if (s[i] != 'a' && s[i] != 'e' && s[i] != 'i' && s[i] != 'o' && s[i] != 'u')
			{
				count++;
			}
			else
			{
				count = 0;
			}
			if (count == 4)
			{
				flag = true;
				break;
			}
		}

		if (flag)
			cout << "NO" << endl;
		else
			cout << "YES" << endl;
	}

	return 0;
}