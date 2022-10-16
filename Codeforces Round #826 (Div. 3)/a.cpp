#include <iostream>
#include <map>
using namespace std;

// XXXS < XS
// XXXL > XL
// XL > M
// XXL = XXL
// XXXXXS < M
// XL > XXXS

map<char, int> m = {{'s', 1}, {'m', 2}, {'l', 3}, {'x', 4}};

int get_shirt_value(string shirt_size)
{
	// get last character
	char shirt_size_char = shirt_size[shirt_size.length() - 1];
	shirt_size_char = tolower(shirt_size_char);
	// get x count
	int x_count = shirt_size.length() - 1;
	// get value
	int value = m[shirt_size_char] * 10000 + x_count;
	return value;
}

int main()
{

	int t;
	cin >> t;
	while (t--)
	{
		string a, b;
		cin >> a >> b;
		int a_value = get_shirt_value(a);
		int b_value = get_shirt_value(b);
		cout << a_value << " " << b_value << endl;
		// print < > or =
		if (a_value < b_value)
		{
			cout << ">" << endl;
		}
		else if (a_value > b_value)
		{
			cout << "<" << endl;
		}
		else
		{
			cout << "=" << endl;
		}
	}

	return 0;
}