#include <iostream>
#include <map>
using namespace std;



int main(){
	
	int t;
	cin >> t;
	while(t--){
		int n;
		cin >> n;
		int a[n];
		map<int,int> m;

		for (int i = 0; i < n; ++i)
		{
			cin >> a[i];
			m[a[i]]++;
		}

		int p = n;

		for (int i = 0; i < n; ++i)
		{
			if (m[a[i]]-1 != 0){
				p = n - (i+1);
				m[a[i]]--;
			}
		}
		cout << n-p << endl;


	}
	

	return 0;
}