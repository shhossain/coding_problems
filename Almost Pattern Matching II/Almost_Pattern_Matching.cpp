#include <iostream>
using namespace std;

int main()
{

	int runs;
	cin >> runs;
	for (int i = 0; i < runs; i++)
	{
		string s, pattern;
		int k;
		cin >> s >> pattern >> k;
		int count = 0;
		for (int i = 0; i < s.length() - pattern.length() + 1; i++)
		{
			int d = 0;
			for (int j = 0; j < pattern.length(); j++)
			{
				if (s[i + j] != pattern[j])
					d++;
			}
			if (d <= k)
				count++;
		}
		cout << count << endl;
	}

	return 0;
}