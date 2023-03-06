#include <iostream>
using namespace std;



int main(){
	int t;
	cin >> t;
	while(t--){
		int n;
		cin >> n;
		int one = 0;
		int other = 0;
		for (int i = 0; i < n; i++){
			int x;
			cin >> x;
			if (x==1){
				one++;
			}
			else{
				other++;
			}
		}


		int total = other + (one/2);

		if (one == 1){
			total++;
		}

		cout << total << endl;
	}


}