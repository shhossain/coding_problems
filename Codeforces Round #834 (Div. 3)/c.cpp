#include <bits/stdc++.h>

using namespace std;

// INPUTS
//  Size 1 - 3
#define i1(a) cin >> a;
#define i2(a, b) cin >> a >> b;
#define i3(a, b, c) cin >> a >> b >> c;

// Size n
#define ivec(vec, n)            \
	for (int i = 0; i < n; i++) \
	{                           \
		int x;                  \
		i1(x);                  \
		vec.push_back(x);       \
	}
#define iarr(arr, n)            \
	for (int i = 0; i < n; i++) \
	{                           \
		int x;                  \
		i1(x);                  \
		arr[i] = x;             \
	}

// Outputs
#define YES cout << "YES" << endl;
#define NO cout << "NO" << endl;
#define print0(a) cout << a;
#define print(a) cout << a << endl;
#define print2(a, b) cout << a << " " << b << endl;

// Loops
#define loop(n) for (int i = 0; i < n; i++)
#define range(a, b) for (int i = a; i < n; i++)
#define rangestep(a, b, step) for (int i = a; i < b; i += step)

int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		int l, r, x, a, b, d1, d2, d3, d4;
		cin >> l >> r >> x;
		cin >> a >> b;

		d1 = abs(a - l);
		d2 = abs(r - a);
		d3 = abs(b - l);
		d4 = abs(r - b);

		if (a == b)
		{
			cout << 0 << endl;
		}
		else if (abs(a - b) >= x)
		{
			cout << 1 << endl;
		}
		else if ((d1 < x && d2 < x) || (d3 < x && d4 < x))
		{
			cout << -1 << endl;
		}
		else
		{
			if (d1 < x)
			{
				if (d4 >= x)
				{
					cout << 2 << endl;
				}
				else
				{
					cout << 3 << endl;
				}
			}
			else if (d2 < x)
			{
				if (d3 >= x)
				{
					cout << 2 << endl;
				}
				else
				{
					cout << 3 << endl;
				}
			}
			else
			{
				cout << 2 << endl;
			}
		}
	}

	return 0;
}