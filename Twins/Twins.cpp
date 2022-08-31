#include <bits/stdc++.h>
using namespace std;

int mincoins(int *arr, int n)
{
	// sort the array in descending order
	sort(arr, arr + n, greater<int>());

	// reverse the array
	int rev[n];
	for (int i = 0; i < n; i++)
	{
		rev[i] = arr[n - i - 1];
	}

	int s = rev[0];
	int c[n] = {s};
	for (int a = 1; a < n; a++)
	{
		s += rev[a];
		c[a] = s;
	}
	// sort descending order
	sort(c, c + n, greater<int>());

	int csum = 0;
	for (int i = 0; i < n; i++)
	{
		csum += arr[i];

		int rsum = c[i + 1];
		if (csum > rsum)
		{
			return i + 1;
		}
	}
	return n;
}

int main()
{
	int runs;
	cin >> runs;
	int arr[runs];
	for (int i = 0; i < runs; i++)
	{
		cin >> arr[i];
	}
	cout << mincoins(arr, runs) << endl;

	return 0;
}