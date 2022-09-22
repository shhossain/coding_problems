#include <bits/stdc++.h>
using namespace std;

int main()
{
	int n;
	cin >> n;
	vector<int> cards(n);
	for (int i = 0; i < n; i++)
		cin >> cards[i];
	// sort array in descending order
	sort(cards.begin(), cards.end(), greater<int>());
	// sorted array in descending order
	cout << "Sorted array in descending order: ";
	for (int i = 0; i < n; i++)
		cout << cards[i] << " ";

	int sereja = 0, dima = 0;
	bool sereja_turn = true;
	bool dima_turn = false;

	for (int i = 0; i < n; i++)
	{
		if (sereja_turn == true)
		{
			sereja += cards[i];
			sereja_turn = false;
			dima_turn = true;
		}
		else if (dima_turn == true)
		{
			dima += cards[i];
			dima_turn = false;
			sereja_turn = true;
		}
	}
	cout << sereja << " " << dima;
	return 0;
}