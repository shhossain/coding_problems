#include <iostream>
#include <algorithm>
using namespace std;

int main(){
	
	int t;
	cin >> t;
	while (t--){
		int n;
		cin >> n;
		int a[n];
		int s[n];
		for (int i = 0; i < n; i++){
			cin >> a[i];
			s[i] = a[i];
		}

		sort(s,s+n);


		int o = 0;
		for (int i = 0; i < n; ++i)
		{
			if (s[i] == 1 && a[i] == 0){
				o++;
			}
		}

		cout << o << endl;

	}
	

	return 0;
}