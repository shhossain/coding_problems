#include <iostream>
using namespace std;


bool hello_in(string s) {
	int h = 0, e = 0, l = 0;
	for (int i = 0; i < s.size(); i++) {
		if (s[i] == 'h') {
			h = 1;
		} else if (s[i] == 'e' && h == 1) {
			e = 1;
		} else if (s[i] == 'l' && h == 1 && e == 1) {
			l++;
		} else if (s[i] == 'o' && h == 1 && e == 1 && l > 1) {
			return true;
		}
	}
	return false;
}

int main()
{
	string s;
	cin >> s;
	if (hello_in(s)) {
		cout << "YES" << endl;
	} else {
		cout << "NO" << endl;
	}
	return 0;
}