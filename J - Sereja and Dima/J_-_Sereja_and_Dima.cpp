// n = input()
// cards = list(map(int, input().split()))
// sereja = 0
// dima = 0
// for i in range(int(n)):
//     if i % 2 == 0:
//         max_num = max(cards[0], cards[-1])
//         sereja += max_num
//         cards.remove(max_num)
//     else:
//         max_num = max(cards[0], cards[-1])
//         dima += max_num
//         cards.remove(max_num)
// print(sereja, dima)

#include <bits/stdc++.h>
using namespace std;

int main() {
	int n;
	cin >> n;
	vector<int> cards(n);
	for (int i = 0; i < n; i++) {
		cin >> cards[i];
	}
	int sereja = 0;
	int dima = 0;
	for (int i = 0; i < n; i++) {
		if (i % 2 == 0) {
			int max_num = max(cards[0], cards[cards.size() - 1]);
			sereja += max_num;
			cards.erase(remove(cards.begin(), cards.end(), max_num), cards.end());
		} else {
			int max_num = max(cards[0], cards[cards.size() - 1]);
			dima += max_num;
			cards.erase(remove(cards.begin(), cards.end(), max_num), cards.end());
		}
	}
	cout << sereja << " " << dima << endl;
}