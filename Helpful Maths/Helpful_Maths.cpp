#include <bits/stdc++.h>
using namespace std;


int main()
{
	// 1+1+3+1+3
	string arr_str;
	cin >> arr_str;
	stringstream ss(arr_str);
	string temp;
	vector<int> arr;
	while (getline(ss, temp, '+'))
	{
		arr.push_back(stoi(temp));
	}
	sort(arr.begin(), arr.end());
	for (int i = 0; i < arr.size(); i++)
	{
		cout << arr[i];
		if (i != arr.size() - 1)
		{
			cout << "+";
		}
	}
	return 0;
}